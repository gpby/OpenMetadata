from metadata.ingestion.source.database.cloudberry.connection import CloudberryConnection
from metadata.ingestion.source.database.cloudberry.lineage import CloudberryLineageSource
from metadata.ingestion.source.database.cloudberry.metadata import CloudberrySource
from metadata.profiler.interface.sqlalchemy.profiler_interface import SQAProfilerInterface
from metadata.sampler.sqlalchemy.sampler import SQASampler
from metadata.utils.importer import get_class_path
from metadata.utils.service_spec.service_spec import BaseSpec

ServiceSpec = BaseSpec(
    metadata_source_class=get_class_path(CloudberrySource),
    lineage_source_class=get_class_path(CloudberryLineageSource),
    connection_class=get_class_path(CloudberryConnection),
    profiler_class=get_class_path(SQAProfilerInterface),
    sampler_class=get_class_path(SQASampler),
)
