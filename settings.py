import os

# -- static settings
version = '1.0.7'
source_system_key = 'UNKNOWN'
source_system_info = 'StopSequences from GeoTours script'
device_key = 'UNKNOWN'


# -- configurable settings (will be set via given arguments or the argument defaults in helpers.py)
env = None
countrykey = None
loginname = None
password = None
nodekey_env_var = None
use_mocked_data = None
use_tourno_as_vehicleno = None
generate_full_sequence = None
plot_created_stop_sequences = None
generate_reduced_sequence = None
keep_every_nth_stop_per_street = None
minutes_till_token_refresh = None
store_json = None
device_profile_key = None
geotourkey = None


# -- folder and file settings
main_script_folder = os.path.dirname(os.path.abspath(__file__))
georoutingpath = main_script_folder + '/inputdata/georouting/georuleexp_*.csv'
geocellpath = main_script_folder + '/inputdata/geocells/geocell*.geojson'
plot_path = main_script_folder + '/plots/'
json_out_path = main_script_folder + '/json_out/stop_sequences.json'

# -- caches
consignees_by_zipcodekeys_list_cache = {}
partneraddresses_by_zipcodekeys_list_cache = {}
partneraddresses_with_routing_cache = {}

# -- static path settings without host
smd_base_path = "seedmasterdataservice/api/v0/"
partner_base_path = "partnerservice/api/v0/"
transport_base_path = "transportservice/api/v0/"
transportflow_base_path = "transportflowservice/api/v0/"
user_base_path = "userservice/api/v0/"


# -- full path settings depending on env

def get_smd_path():
    """Construct and return SMD path depending on environment (in docker container or from outside)

    :return: path string
    """

    if env == "DOCKER":
        return "http://parcelos-seedmasterdata:8080/" + smd_base_path
    else:
        return "http://localhost:8090/" + smd_base_path


def get_partner_path():
    """Construct and return partner path depending on environment (in docker container or from outside)

    :return: path string
    """

    if env == "DOCKER":
        return "http://parcelos-partner:8080/" + partner_base_path
    else:
        return "http://localhost:8090/" + partner_base_path


def get_transport_path():
    """Construct and return transport path depending on environment (in docker container or from outside)

    :return: path string
    """

    if env == "DOCKER":
        return "http://parcelos-transport:8080/" + transport_base_path
    else:
        return "http://localhost:8090/" + transport_base_path


def get_transportflow_path():
    """Construct and return transportflow path depending on environment (in docker container or from outside)

    :return: path string
    """

    if env == "DOCKER":
        return "http://parcelos-transport-flow:8080/" + transportflow_base_path
    else:
        return "http://localhost:8090/" + transportflow_base_path


def get_user_path():
    """Construct and return user path depending on environment (in docker container or from outside)

    :return: path string
    """

    if env == "DOCKER":
        return "http://parcelos-user:8080/" + user_base_path
    else:
        return "http://localhost:8090/" + user_base_path


# -- indentation for lof messages
indent1 = '  '
indent2 = '    '
indent3 = '      '
