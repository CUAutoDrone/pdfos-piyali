# Necessary Libraries

# API Info from ENV
from dotenv import load_dotenv
import os
import time
import zipfile
import re
import payloads

import isodate
import urllib3
import pandas as pd
import numpy as np

# Simscale Imports
from simscale_sdk import Configuration, ApiClient, ProjectsApi, StorageApi, GeometryImportsApi, GeometriesApi, \
    MeshOperationsApi, SimulationsApi, SimulationRunsApi, ReportsApi, Project, GeometryImportRequest, ApiException, \
    MaterialsApi, MaterialGroupType, MaterialUpdateRequest, MaterialUpdateOperation, MaterialUpdateOperationReference
from simscale_sdk import GeometryImportRequestLocation, GeometryImportRequestOptions, Point, DimensionalVectorLength, \
    DecimalVector
from simscale_sdk import Incompressible, IncompressibleFluidMaterials, FluidModel, FluidInitialConditions, \
    AdvancedConcepts, TopologicalReference, FluidNumerics, RelaxationFactor, DimensionalPressure, \
    ProbePointsResultControl, \
    ResidualControls, Tolerance, FluidSolvers, Schemes, TimeDifferentiationSchemes, GradientSchemes, DivergenceSchemes, \
    LaplacianSchemes, InterpolationSchemes, SurfaceNormalGradientSchemes, SlipVBC, VelocityInletBC, WallBC, SymmetryBC, NoSlipVBC, FixedValueVBC, \
    ComponentVectorFunction, ConstantFunction, PressureOutletBC, FixedValuePBC, DimensionalFunctionPressure, \
    FluidSimulationControl, DimensionalTime, TimeStepWriteControl, DimensionalArea, ScotchDecomposeAlgorithm, FluidResultControls, \
    DimensionalVectorFunctionSpeed, ForcesMomentsResultControl, ForceMomentCoefficientsResultControl, DimensionalSpeed, OneOfTimeDifferentiationSchemesForDefault
from simscale_sdk import SimulationSpec, MeshOperation, SimmetrixMeshingFluid, AutomaticLayerOn, SimulationRun
from simscale_sdk import TopViewPredefinedCameraSettings, ProjectionType, Vector3D, ModelSettings, Filters, ScalarField, \
    ResolutionInfo, ReportRequest, TimeStepAnimationOutputSettings, AnimationReportProperties, CuttingPlane, RenderMode

# Onshape Import
from onshape_client.client import Client


# Setup api's for a run
def setup_api_clints(simscale_api_key_env_name, simscale_api_url="https://api.simscale.com"):
  
  # Check that the environment variables are set
  load_dotenv()

  # Simscale API client configuration
  simscale_api_key = os.getenv(simscale_api_key_env_name)
  simscale_api_url = simscale_api_url
  simscale_api_key_header = "X-API-KEY"

  configuration = Configuration()
  configuration.debug = True
  configuration.host = simscale_api_url + "/v0"
  configuration.api_key = {
      simscale_api_key_header: simscale_api_key
  }

  # Get Main Simscale Client
  simscale_api_client = ApiClient(configuration)

  retry_policy = urllib3.Retry(connect=5, read=5, redirect=0, status=5, backoff_factor=0.2)
  simscale_api_client.rest_client.pool_manager.connection_pool_kw["retries"] = retry_policy

  # Simscale API clients
  project_api = ProjectsApi(simscale_api_client)
  storage_api = StorageApi(simscale_api_client)
  geometry_import_api = GeometryImportsApi(simscale_api_client)
  geometry_api = GeometriesApi(simscale_api_client)
  mesh_operation_api = MeshOperationsApi(simscale_api_client)
  simulation_api = SimulationsApi(simscale_api_client)
  simulation_run_api = SimulationRunsApi(simscale_api_client)
  reports_api = ReportsApi(simscale_api_client)
  materials_api = MaterialsApi(simscale_api_client)

  # Onshape API Client
  access_key = "m0gYBcdS7XDGVEN6P6ZOnCKV"
  secret_key = "z7yhjr1vU2CCAUTdKv8iaElUW7Y6XqMXaIlLeP06SioI7Jms"
  base = "https://cuautodrone.onshape.com/"
  onshape_client = Client(configuration={"base_url":base,
                                "access_key":access_key,
                                "secret_key":secret_key})
  
  return {"simscale_client": simscale_api_client, "project_api":project_api, "storage_api":storage_api, "geometry_import_api":geometry_import_api,
          "geometry_api":geometry_api, "mesh_operation_api":mesh_operation_api, "simulation_api":simulation_api,
          "simulation_run_api":simulation_run_api, "reports_api":reports_api, "materials_api":materials_api,
          "onshape_client":onshape_client}, simscale_api_url, base


##################################### ONSHAPE #################################################

# Set Feature Values
def set_feature_vals(onshape_api, onshape_api_base_url, feature_dict, did, wid, eid):
   
   for feature_id in list(feature_dict.keys()):
        print(feature_id)
        payload = feature_dict[feature_id]
        fixed_url = "api/v9/partstudios/d/"+did+"/w/"+wid+"/e/"+eid+"/features/featureid/"+feature_id
        final_url = onshape_api_base_url + fixed_url
        method = 'POST'
        params = {}
        headers = {'Accept': 'application/json;charset=UTF-8; qs=0.09',
            'Authorization': 'Basic CREDENTIALS',
            'Content-Type': "application/json;charset=UTF-8; qs=0.09"}

        _ = onshape_api.api_client.request(method, url=final_url, query_params=params, headers=headers,
                                            body=payload)


# Get Variables for measured stuff
def get_variables(onshape_api, onshape_api_base_url, did, wid, eid):

  method = "GET"
  final_url = onshape_api_base_url+"api/v9/variables/d/"+did+"/w/"+wid+"/e/"+eid+"/variables" 
  params = {"includeValuesAndReferencedVariables":True}
  headers = {'Accept': 'application/json;charset=UTF-8; qs=0.09',
            'Authorization': 'Basic CREDENTIALS',
            'Content-Type': "application/json;charset=UTF-8; qs=0.09"}

  response = onshape_api.api_client.request(method, url=final_url, query_params=params,headers=headers,body={})
  return response.data


# Get measured diameter value for reference area
def get_reference_area(onshape_api, onshape_api_base_url, did, wid, eid, index_string, re_string):

  variable_data = get_variables(onshape_api, onshape_api_base_url, did, wid, eid)
  index = variable_data.index(index_string)
  diameter_string = variable_data[index:]
  my_match = re.search(re_string, diameter_string)
  measured_radius = float(my_match.group(0)[12:-7])/2
  reference_area = np.pi * (measured_radius**2)
  return measured_radius, reference_area


# Get part info
def get_get_part_info(onshape_api, onshape_api_base_url, did, wid, eid):

  fixed_url = "api/v9/parts/d/"+did+"/w/"+wid+"/e/"+eid
  final_url = onshape_api_base_url+fixed_url

  method = 'GET'

  params = {}
  payload = {}
  headers = {'Accept': 'application/json;charset=UTF-8; qs=0.09', 'Authorization': 'Basic CREDENTIALS'}

  response = onshape_api.api_client.request(method, url=final_url, query_params=params, headers=headers, body=payload)
  return response.data


# Get part id
def get_part_id(onshape_api, onshape_api_base_url, did, wid, eid, index_string, re_string):

  part_string = get_get_part_info(onshape_api, onshape_api_base_url, did, wid, eid)
  index = part_string.index(index_string)
  aero_shell_string = part_string[index:]
  my_match = re.search(re_string, aero_shell_string)
  pid = my_match.group(0)[12:-1]
  return pid


# Download onshape file
def download_onshape_file(onshape_api, onshape_api_base_url, did, wid, eid, file_name, index_string, re_string):
  
  pid = get_part_id(onshape_api, onshape_api_base_url, did, wid, eid, index_string, re_string)
  fixed_url = "api/v9/parts/d/"+did+"/w/"+wid+"/e/"+eid+"/partid/"+pid+"/parasolid"
  cad_final_url = onshape_api_base_url+fixed_url

  method = 'GET'

  params = {}
  payload = {}
  headers = {'accept': '*/*'}

  response = onshape_api.api_client.request(method, url=cad_final_url, query_params=params, headers=headers, body=payload)

  with open(file_name, mode="w") as file:
    file.write(response.data)



################################# SIMSCALE ########################################
# Initialize Project
def initialize_project(project_api, project_name, project_description, project_measurement="SI"):
  # Create project
  project = Project(
      name=project_name, description=project_description, measurement_system=project_measurement
  )
  project = project_api.create_project(project)
  project_id = project.project_id
  print(f"projectId: {project_id}")

  # Read project information and update with the deserialized model
  project = project_api.get_project(project_id)
  project_api.update_project(project_id, project)
  return project, project_id

# Upload geometry
def upload_cad_geometry(storage_api, geometry_import_api, simscale_api_client, geometry_api, project_id, filename, geometry_name):
   
  # Upload CAD
  storage = storage_api.create_storage()
  with open(filename, "rb") as file:
      simscale_api_client.rest_client.PUT(url=storage.url, headers={"Content-Type": "application/octet-stream"}, body=file.read())
  storage_id = storage.storage_id
  print(f"storage_id: {storage_id}")

  # Import CAD
  geometry_import = GeometryImportRequest(
      name=geometry_name,
      location=GeometryImportRequestLocation(storage_id),
      format="PARASOLID",
      input_unit="m",
      options=GeometryImportRequestOptions(facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=False),
  )

  geometry_import = geometry_import_api.import_geometry(project_id, geometry_import)
  geometry_import_id = geometry_import.geometry_import_id
  geometry_import_start = time.time()
  while geometry_import.status not in ("FINISHED", "CANCELED", "FAILED"):
      # adjust timeout for larger geometries
      if time.time() > geometry_import_start + 900:
          raise TimeoutError()
      time.sleep(10)
      geometry_import = geometry_import_api.get_geometry_import(project_id, geometry_import_id)
      print(f"Geometry import status: {geometry_import.status}")
  geometry_id = geometry_import.geometry_id
  print(f"geometry_id: {geometry_id}")

  # Read geometry information and update with the deserialized model
  geometry = geometry_api.get_geometry(project_id, geometry_id)
  geometry_api.update_geometry(project_id, geometry_id, geometry)

  return geometry, geometry_id, storage, storage_id

# Create Boundary Conditions
def get_single_entity_name(geometry_api, project_id, geometry_id, **kwargs):
    
  entities = geometry_api.get_geometry_mappings(project_id, geometry_id, **kwargs).embedded
  if len(entities) == 1:
      return entities[0].name
  else:
      raise Exception(f"Found {len(entities)} entities instead of 1: {entities}")


def get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs):
   
  entity_list = []
  for entity in entities:
    entity_list.append(get_single_entity_name(geometry_api, project_id, geometry_id, entities=[entity]), **kwargs)
  return entity_list

# Velocity
def create_velocity_inlet(name, vel_vec, entities, geometry_api, project_id, geometry_id, **kwargs):
   
  entity_list = get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs)

  inlet_bc = VelocityInletBC(
            name=name,
            velocity=FixedValueVBC(
                value=DimensionalVectorFunctionSpeed(
                    value=vel_vec
                )
            ),
            topological_reference=TopologicalReference(entities=entity_list),
        )
  
  return inlet_bc
  
# Presure
def create_pressure_outlet(name, gauge_pressure, entities, geometry_api, project_id, geometry_id, **kwargs):
   
  entity_list = get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs)
  outlet_bc = PressureOutletBC(
            name=name,
            gauge_pressure=FixedValuePBC(value=DimensionalFunctionPressure(value=ConstantFunction(value=gauge_pressure), unit="Pa")),
            topological_reference=TopologicalReference(entities=entity_list),
        )
  return outlet_bc

# Symmetry
def create_symmetry_wall(name, entities, geometry_api, project_id, geometry_id, **kwargs):
   
  entity_list = get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs)
  symmetry_bc = SymmetryBC(
            name=name,
            topological_reference=TopologicalReference(entities=entity_list)
  )
   
# Slip
def create_slip_wall(name, entities, geometry_api, project_id, geometry_id, **kwargs):
   
  entity_list = get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs)
  slip_wall_bcs = WallBC(name = name, velocity = SlipVBC(), topological_reference = TopologicalReference(entities = entity_list))
  return slip_wall_bcs

# No Slip
def create_noslip_wall(name, entities, geometry_api, project_id, geometry_id, **kwargs):

  entity_list = get_entity_list(entities, geometry_api, project_id, geometry_id, **kwargs)
  no_slip_wall = WallBC(name = name, velocity = NoSlipVBC(turbulence_wall="WALL_FUNCTION"), topological_reference = TopologicalReference(entities = entity_list))
  return no_slip_wall



# Generate Model
def generate_model(simulation_api, simulation_spec_name, geometry_id, project_id, boundary_conditions, drone_airspeed, 
                   reference_area, drag_measurement_entity, lift_dir, drag_dir):
  model = Incompressible(
    model=FluidModel(),
    initial_conditions=FluidInitialConditions(),
    advanced_concepts=AdvancedConcepts(),
    materials=IncompressibleFluidMaterials(),
    numerics=FluidNumerics(
        relaxation_factor=RelaxationFactor(),
        pressure_reference_value=DimensionalPressure(value=0, unit="Pa"),
        residual_controls=ResidualControls(
            velocity=Tolerance(),
            pressure=Tolerance(),
            turbulent_kinetic_energy=Tolerance(),
            omega_dissipation_rate=Tolerance(),
        ),
        solvers=FluidSolvers(),
        schemes=Schemes(
            time_differentiation=TimeDifferentiationSchemes(
              for_default = OneOfTimeDifferentiationSchemesForDefault(type = 'STEADYSTATE')),
            gradient=GradientSchemes(),
            divergence=DivergenceSchemes(),
            laplacian=LaplacianSchemes(),
            interpolation=InterpolationSchemes(),
            surface_normal_gradient=SurfaceNormalGradientSchemes(),
        ),
    ),
    boundary_conditions=boundary_conditions,
    simulation_control=FluidSimulationControl(
        end_time=DimensionalTime(value=200, unit="s"),
        delta_t=DimensionalTime(value=1, unit="s"),
        write_control=TimeStepWriteControl(write_interval=20),
        max_run_time=DimensionalTime(value=10000, unit="s"),
        decompose_algorithm=ScotchDecomposeAlgorithm(),
    ),
    result_control = FluidResultControls(forces_moments=[
            ForceMomentCoefficientsResultControl(
                name="Forces and moments coefficients",
                lift_direction = lift_dir, #based on input velociy vector and orientation of design
                drag_direction = drag_dir, #based on input velociy vector and orientation of design
                freestream_velocity_magnitude = DimensionalSpeed(value = drone_airspeed, unit = "m/s"), #drone airspeed
                write_control=TimeStepWriteControl(write_interval=1),
                topological_reference=TopologicalReference(entities=drag_measurement_entity),
                reference_area_value = DimensionalArea(value = reference_area, unit = "m^2")
            )
        ]),
  )

  simulation_spec = SimulationSpec(name=simulation_spec_name, geometry_id=geometry_id, model=model)
  # Create simulation
  simulation_id = simulation_api.create_simulation(project_id, simulation_spec).simulation_id
  print(f"simulation_id: {simulation_id}")

  return simulation_id


# Generate Air Materials
def define_air(materials_api, simulation_api, project_id, simulation_id, volume_entity):
  # Add a material to the simulation
  material_groups = materials_api.get_material_groups().embedded
  default_material_group = next((group for group in material_groups if group.group_type == MaterialGroupType.SIMSCALE_DEFAULT), None)
  if not default_material_group:
      raise Exception(f"Couldn't find default material group in {material_groups}")

  default_materials = materials_api.get_materials(material_group_id=default_material_group.material_group_id).embedded
  material_air = next((material for material in default_materials if material.name == "Air"), None)
  if not material_air:
      raise Exception(f"Couldn't find default Air material in {default_materials}")

  material_data = materials_api.get_material_data(
      material_group_id=default_material_group.material_group_id,
      material_id=material_air.id
  )
  material_update_request = MaterialUpdateRequest(
      operations=[
          MaterialUpdateOperation(
              path="/materials/fluids",
              material_data=material_data,
              reference=MaterialUpdateOperationReference(
                  material_group_id=default_material_group.material_group_id,
                  material_id=material_air.id
              )
          )
      ]
  )
  material_update_response = simulation_api.update_simulation_materials(project_id, simulation_id, material_update_request)

  # Add assignments to the new material
  simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
  simulation_spec.model.materials.fluids[0].topological_reference = TopologicalReference(entities=volume_entity)
  simulation_api.update_simulation(project_id, simulation_id, simulation_spec)
  return material_update_response


# Generate Mesh
def generate_mesh(mesh_operation_api, simulation_api, mesh_name, project_id, geometry_id, simulation_id):

   # Start of mesh operation
  mesh_operation = mesh_operation_api.create_mesh_operation(
      project_id,
      MeshOperation(
          name=mesh_name,
          geometry_id=geometry_id,
          model=SimmetrixMeshingFluid(physics_based_meshing=True, automatic_layer_settings=AutomaticLayerOn()),
      ),
  )
  mesh_operation_api.update_mesh_operation(project_id, mesh_operation.mesh_operation_id, mesh_operation)
  mesh_operation_id = mesh_operation.mesh_operation_id

  mesh_check = mesh_operation_api.check_mesh_operation_setup(project_id, mesh_operation_id, simulation_id=simulation_id)
  warnings = [entry for entry in mesh_check.entries if entry.severity == "WARNING"]
  print(f"Meshing check warnings: {warnings}")
  errors = [entry for entry in mesh_check.entries if entry.severity == "ERROR"]
  if errors:
      raise Exception("Meshing check failed", mesh_check)

  # Estimate Mesh operation
  try:
      mesh_estimation = mesh_operation_api.estimate_mesh_operation(project_id, mesh_operation_id)
      print(f"Mesh operation estimation: {mesh_estimation}")

      if mesh_estimation.compute_resource is not None and mesh_estimation.compute_resource.value > 10.0:
          raise Exception("Too expensive", mesh_estimation)

      if mesh_estimation.duration is not None:
          mesh_max_runtime = isodate.parse_duration(mesh_estimation.duration.interval_max).total_seconds()
          mesh_max_runtime = max(3600, mesh_max_runtime * 2)
      else:
          mesh_max_runtime = 36000
          print(f"Mesh operation estimated duration not available, assuming max runtime of {mesh_max_runtime} seconds")
  except ApiException as ae:
      if ae.status == 422:
          mesh_max_runtime = 36000
          print(f"Mesh operation estimation not available, assuming max runtime of {mesh_max_runtime} seconds")
      else:
          raise ae

  mesh_operation_api.start_mesh_operation(project_id, mesh_operation_id, simulation_id=simulation_id)

  # Wait until the meshing operation is complete
  mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
  mesh_operation_start = time.time()
  while mesh_operation.status not in ("FINISHED", "CANCELED", "FAILED"):
      if time.time() > mesh_operation_start + mesh_max_runtime:
          raise TimeoutError()
      time.sleep(30)
      mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
      print(f"Meshing run status: {mesh_operation.status} - {mesh_operation.progress}")

  mesh_operation = mesh_operation_api.get_mesh_operation(project_id, mesh_operation_id)
  print(f"final mesh_operation: {mesh_operation}")

  # Get the simulation spec and update it with mesh_id from the previous mesh operation
  simulation_spec = simulation_api.get_simulation(project_id, simulation_id)
  simulation_spec.mesh_id = mesh_operation.mesh_id
  simulation_api.update_simulation(project_id, simulation_id, simulation_spec)


# Run simulation
def run_simulation(simulation_api, simulation_run_api, project_id, simulation_id):

  # Check simulation
  check = simulation_api.check_simulation_setup(project_id, simulation_id)
  warnings = [entry for entry in check.entries if entry.severity == "WARNING"]
  print(f"Simulation check warnings: {warnings}")
  errors = [entry for entry in check.entries if entry.severity == "ERROR"]
  if errors:
      raise Exception("Simulation check failed", check)

  # Estimate simulation
  try:
      estimation = simulation_api.estimate_simulation_setup(project_id, simulation_id)
      print(f"Simulation estimation: {estimation}")

      if estimation.compute_resource is not None and estimation.compute_resource.value > 10.0:
          raise Exception("Too expensive", estimation)

      if estimation.duration is not None:
          max_runtime = isodate.parse_duration(estimation.duration.interval_max).total_seconds()
          max_runtime = max(3600, max_runtime * 2)
      else:
          max_runtime = 36000
          print(f"Simulation estimated duration not available, assuming max runtime of {max_runtime} seconds")
  except ApiException as ae:
      if ae.status == 422:
          max_runtime = 36000
          print(f"Simulation estimation not available, assuming max runtime of {max_runtime} seconds")
      else:
          raise ae

  # Create simulation run
  simulation_run = SimulationRun(name="Run 1")
  simulation_run = simulation_run_api.create_simulation_run(project_id, simulation_id, simulation_run)
  run_id = simulation_run.run_id
  print(f"runId: {run_id}")

  # Read simulation run and update with the deserialized model
  simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
  simulation_run_api.update_simulation_run(project_id, simulation_id, run_id, simulation_run)

  # Start simulation run and wait until it's finished
  simulation_run_api.start_simulation_run(project_id, simulation_id, run_id)
  simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
  simulation_run_start = time.time()
  while simulation_run.status not in ("FINISHED", "CANCELED", "FAILED"):
      if time.time() > simulation_run_start + max_runtime:
          raise TimeoutError()
      time.sleep(30)
      simulation_run = simulation_run_api.get_simulation_run(project_id, simulation_id, run_id)
      print(f"Simulation run status: {simulation_run.status} - {simulation_run.progress}")

  return run_id


# Get drag value
def get_drag_lift_coeff(simscale_api_client, simscale_api_key_env_name,
                   simulation_run_api, project_id, simulation_id, run_id):

   # Download force coefficient solution fields
  force_coef_solution_fields_results = simulation_run_api.get_simulation_run_results(
      project_id,
      simulation_id,
      run_id,
      page=1,
      limit=100,
      category="FORCE_COEFFICIENTS_PLOT"
  )
  print(f"Solution Force Coefficient results: {force_coef_solution_fields_results}")

  simscale_api_key_header = "X-API-KEY"
  simscale_api_key = os.getenv(simscale_api_key_env_name)

  force_info = force_coef_solution_fields_results.embedded[0]
  force_data_response = simscale_api_client.rest_client.GET(
      url=force_info.download.url,
      headers={simscale_api_key_header: simscale_api_key},
      _preload_content=False,
  )

  force_data_csv = force_data_response.data.decode("utf-8")
  print(f"Area average data as CSV: {force_data_csv}")

  with open("force_coef_data.csv", "w") as f:
    f.write(force_data_csv)

  df = pd.read_csv("force_coef_data.csv")
  drag_coef_column = df["FORCE_COEFFICIENT_CD"]
  drag_coef = drag_coef_column.tail(n = 1).item()
  lift_coef_column = df["FORCE_COEFFICIENT_CL"]
  lift_coef = lift_coef_column.tail(n = 1).item()

  return drag_coef, lift_coef



def main_run(body_parameter_values):
   
  api_client_dict, simscale_url, onshape_url = setup_api_clints("SIMSCALE_API_KEY")
   



  ############## NEED TO GET THIS BEFORE RUN ####################
  did = "8cc415b7a80196497cd537a4"
  wid = "2d2e7365b615264c75bb21d4"
  eid = "bcc58dd1c00017056413bb9d"

  # Params for body
  c1 = "FVJX0qmQg48MNre_0"
  c2 = "Fgz4GyXRtwO8Vli_0"
  c3 = "FTKV8r7d8hr5kme_0"
  c4 = "Fwnh8qJNpq0GQaW_0"

  feature_dict = {
     c1 : payloads.return_payload_feature1_dict(c1, body_parameter_values[0]),
     c2 : payloads.return_payload_feature2_dict(c2, body_parameter_values[1]),
     c3 : payloads.return_payload_feature3_dict(c3, body_parameter_values[2]),
     c4 : payloads.return_payload_feature4_dict(c4, body_parameter_values[3])
  }

  area_index_string = '"name" : "Xdiameter"'
  area_re_string = r'"value" : ".*"'

  download_index_string = '"name" : "Part 1"'
  download_re_string = r'"partId" : ".*"'

  cad_filename = "aerobody_test.x_t"
  #################################################################




  set_feature_vals(api_client_dict["onshape_client"], onshape_url, feature_dict, did, wid, eid)

  reference_area = get_reference_area(api_client_dict["onshape_client"], onshape_url, did, wid, eid, area_index_string,
                                      area_re_string)
  
  download_onshape_file(api_client_dict["onshape_client"], onshape_url, did, wid, eid, cad_filename, 
                        download_index_string, download_re_string)
  
  project, project_id = initialize_project(api_client_dict["project_api"], "AerobodyTest", "Test Simulation of Simple Aero Body")

  geometry, geometry_id, storage, storage_id = upload_cad_geometry(api_client_dict["storage_api"], 
                                                                   api_client_dict["geometry_import_api"],
                                                                   api_client_dict["simscale_client"],
                                                                   api_client_dict["geometry_api"], project_id,
                                                                   cad_filename, "CAD Geometry")
  


  ############################ Entity Names NEED THIS BEFORE RUN ##########################
  volume_entity = "region0-9-0-3"
  aero_face_entity = "10-0-2"
  inlet_entity = "9-2-2"
  outlet_entity = "9-1-2"
  symmetry_entities = ["10-1-2", "10-2-2"]
  slip_wall_entities = ["9-3-2", "9-5-2"]

  drone_airspeed = 0.5
  drone_vel_vec = ComponentVectorFunction(x=ConstantFunction(value=0), y=ConstantFunction(value=-1*drone_airspeed), z=ConstantFunction(value=0))

  lift_dir = DimensionalVectorLength(value = DecimalVector(x=0.0,y=0.0,z=1.0), unit = "m")
  drag_dir = DimensionalVectorLength(value = DecimalVector(x=0.0,y=-1.0,z=0.0), unit = "m")
  ##########################################################################################




  volume = get_entity_list([volume_entity], api_client_dict["geometry_api"], project_id, geometry_id)
  aero_face = get_entity_list([aero_face_entity], api_client_dict["geometry_api"], project_id, geometry_id)

  inlet_bc = create_velocity_inlet("Velocity Inlet", drone_vel_vec, [inlet_entity], api_client_dict["geometry_api"], project_id, geometry_id)
  outlet_bc = create_pressure_outlet("Pressure Outlet", 0, [outlet_entity], api_client_dict["geometry_api"], project_id, geometry_id)
  symmetry_bc = create_symmetry_wall("Symmetry Walls", symmetry_entities, api_client_dict["geometry_api"], project_id, geometry_id)
  no_slip_bc = create_noslip_wall("No Slip Face", [aero_face_entity], api_client_dict["geometry_api"], project_id, geometry_id)
  slip_bc = create_slip_wall("Slip Walls", slip_wall_entities, api_client_dict["geometry_api"], project_id, geometry_id)

  boundary_conditions = [inlet_bc, outlet_bc, symmetry_bc, no_slip_bc, slip_bc]

  simulation_id = generate_model(api_client_dict["simulation_api"], "AeroBody Sim", geometry_id, 
                                 project_id, boundary_conditions, drone_airspeed, reference_area, aero_face,
                                 lift_dir, drag_dir)
  
  material_response = define_air(api_client_dict["materials_api"], api_client_dict["simulation_api"], project_id, simulation_id, volume)
  generate_mesh(api_client_dict["mesh_operation_api"], api_client_dict["simulation_api"], "AeroBody Mesh", project_id, geometry_id, simulation_id)

  run_id = run_simulation(api_client_dict["simulation_api"], api_client_dict["simulation_run_api"], project_id, simulation_id)

  lift_coef, drag_coef = get_drag_lift_coeff(api_client_dict["simscale_client"], "SIMSCALE_API_KEY", api_client_dict["simulation_run_api"], project_id, simulation_id, run_id)


  return lift_coef, drag_coef, dict(zip(["c1", "c2", "c3", "c4"], body_parameter_values)), reference_area, drone_airspeed