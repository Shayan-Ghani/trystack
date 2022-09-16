import pytest
from json import load as json_load
from os.path import isfile
def test_config_file(app_client, config_client):
    config_file= "/home/shayan/trystack/trystack/files/config.json"
    assert isfile(config_file) == True
    app_client(config_file=config_file)
    with open(config_file, "r") as file:  
        try:
            config_dict = json_load(file)
        except Exception as e:
            assert e
        config_client.from_file(config_file, load=json_load)    
        assert config_client["TESTING"] == config_dict["TESTING"]
        assert config_client["ENV"] == config_dict["ENV"]
        assert config_client["DEBUG"] == config_dict["DEBUG"]
        assert config_client["SQLALCHEMY_DATABASE_URI"] == config_dict["SQLALCHEMY_DATABASE_URI"]
        assert config_client["SQLALCHEMY_RECORD_MODIFICATIONS"] == config_dict["SQLALCHEMY_RECORD_MODIFICATIONS"]
        assert config_client["SQLALCHEMY_RECORD_QUERIES"] == config_dict["SQLALCHEMY_RECORD_QUERIES"]
        assert config_client["SQLALCHEMY_ECHO"] == config_dict["SQLALCHEMY_ECHO"]
        assert config_client["DEFAULT_PROJECT_STATUS"] == config_dict["DEFAULT_PROJECT_STATUS"]
        assert config_file.endswith(".json") == True
