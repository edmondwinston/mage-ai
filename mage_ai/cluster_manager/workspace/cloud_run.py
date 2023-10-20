import os

import yaml

from mage_ai.cluster_manager.constants import GCP_PROJECT_ID
from mage_ai.cluster_manager.gcp.cloud_run_service_manager import CloudRunServiceManager
from mage_ai.cluster_manager.workspace.base import Workspace
from mage_ai.shared.hash import merge_dict


class CloudRunWorkspace(Workspace):
    def __init__(self, name: str):
        super().__init__(name)
        self.cloud_run_service_manager = CloudRunServiceManager(
            self.config.get('project_id', os.getenv(GCP_PROJECT_ID)),
            self.config.get('path_to_credentials', os.getenv('path_to_keyfile')),
            region=self.config.get('region', os.getenv('GCP_REGION')),
        )

    @classmethod
    def initialize(
        cls,
        name: str,
        config_path: str,
        **kwargs,
    ) -> Workspace:
        project_id = kwargs.get('project_id', os.getenv(GCP_PROJECT_ID))
        path_to_credentials = kwargs.get(
            'path_to_credentials', os.getenv('path_to_keyfile')
        )
        region = kwargs.get('region', os.getenv('GCP_REGION'))

        if config_path:
            with open(config_path, 'w', encoding='utf-8') as fp:
                yaml.dump(
                    merge_dict(
                        kwargs,
                        dict(
                            project_id=project_id,
                            path_to_credentials=path_to_credentials,
                            region=region,
                        ),
                    ),
                    fp,
                )

        cloud_run_service_manager = CloudRunServiceManager(
            project_id, path_to_credentials, region=region
        )

        cloud_run_service_manager.create_service(name)

        return cls(name)

    def delete(self, **kwargs):
        raise NotImplementedError('Delete not implemented for Cloud Run')

    def update(self, **kwargs):
        raise NotImplementedError('Update not implemented for Cloud Run')
