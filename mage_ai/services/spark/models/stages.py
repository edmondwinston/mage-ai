from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List

from mage_ai.services.spark.models.base import BaseSparkModel


class Locality(str, Enum):
    NODE_LOCAL = 'NODE_LOCAL'
    PROCESS_LOCAL = 'PROCESS_LOCAL'


class StageStatus(str, Enum):
    COMPLETE = 'COMPLETE'


class TaskStatus(str, Enum):
    SUCCESS = 'SUCCESS'


@dataclass
class Metrics(BaseSparkModel):
    direct_pool_memory: int = None  # 0
    jvm_heap_memory: int = None  # 0
    jvm_off_heap_memory: int = None  # 0
    major_gc_count: int = None  # 0
    major_gc_time: int = None  # 0
    mapped_pool_memory: int = None  # 0
    minor_gc_count: int = None  # 0
    minor_gc_time: int = None  # 0
    off_heap_execution_memory: int = None  # 0
    off_heap_storage_memory: int = None  # 0
    off_heap_unified_memory: int = None  # 0
    on_heap_execution_memory: int = None  # 0
    on_heap_storage_memory: int = None  # 0
    on_heap_unified_memory: int = None  # 0
    process_tree_jvmrss_memory: int = None  # 0
    process_tree_jvmv_memory: int = None  # 0
    process_tree_other_rss_memory: int = None  # 0
    process_tree_other_v_memory: int = None  # 0
    process_tree_python_rss_memory: int = None  # 0
    process_tree_python_v_memory: int = None  # 0
    total_gc_time: int = None  # 0


@dataclass
class Driver(BaseSparkModel):
    disk_bytes_spilled: int = None  # 0
    failed_tasks: int = None  # 0
    input_bytes: int = None  # 0
    input_records: int = None  # 0
    is_blacklisted_for_stage: bool = None  # false
    is_excluded_for_stage: bool = None  # false
    killed_tasks: int = None  # 0
    memory_bytes_spilled: int = None  # 0
    output_bytes: int = None  # 0
    output_records: int = None  # 0
    peak_memory_metrics: Metrics = None  # {}
    shuffle_read: int = None  # 59
    shuffle_read_records: int = None  # 1
    shuffle_write: int = None  # 0
    shuffle_write_records: int = None  # 0
    succeeded_tasks: int = None  # 1
    task_time: int = None  # 11

    def __post_init__(self):
        if self.peak_memory_metrics:
            self.peak_memory_metrics = Metrics.load(**self.peak_memory_metrics)


@dataclass
class ExecutorSummary(BaseSparkModel):
    driver: Driver = None

    def __post_init__(self):
        if self.driver:
            self.driver = Driver.load(**self.driver)


@dataclass
class InputMetrics(BaseSparkModel):
    bytes_read: int = None  # 0
    records_read: int = None  # 0


@dataclass
class OutputMetrics(BaseSparkModel):
    bytes_written: int  # 0
    records_written: int  # 0


@dataclass
class PushReadMetrics(BaseSparkModel):
    corruptMergedBlockChunks: int = None  # 0
    localMergedBlocksFetched: int = None  # 0
    localMergedBytesRead: int = None  # 0
    localMergedChunksFetched: int = None  # 0
    mergedFetchFallbackCount: int = None  # 0
    remoteMergedBlocksFetched: int = None  # 0
    remoteMergedBytesRead: int = None  # 0
    remoteMergedChunksFetched: int = None  # 0
    remoteMergedReqsDuration: int = None  # 0


@dataclass
class ShuffleReadMetrics(BaseSparkModel):
    fetch_wait_time: int = None  # 0
    local_blocks_fetched: int = None  # 1
    local_bytes_read: int = None  # 59
    records_read: int = None  # 1
    remote_blocks_fetched: int = None  # 0
    remote_bytes_read: int = None  # 0
    remote_bytes_read_to_disk: int = None  # 0
    remote_reqs_duration: int = None  # 0
    shuffle_push_read_metrics: PushReadMetrics = None

    def __post_init__(self):
        if self.shuffle_push_read_metrics:
            self.shuffle_push_read_metrics = PushReadMetrics(self.shuffle_push_read_metrics)


@dataclass
class ShuffleWriteMetrics(BaseSparkModel):
    bytes_written: int = None  # 0
    records_written: int = None  # 0
    write_time: int = None  # 0


@dataclass
class TaskMetrics(BaseSparkModel):
    disk_bytes_spilled: int = None  # 0
    executor_cpu_time: int = None  # 1442666
    executor_deserialize_cpu_time: int = None  # 988667
    executor_deserialize_time: int = None  # 0
    executor_run_time: int = None  # 8
    input_metrics: InputMetrics = None
    jvm_gc_time: int = None  # 0
    memory_bytes_spilled: int = None  # 0
    output_metrics: OutputMetrics = None
    peak_execution_memory: int = None  # 0
    result_serialization_time: int = None  # 0
    result_size: int = None  # 3952
    shuffle_read_metrics: ShuffleReadMetrics = None
    shuffle_write_metrics: ShuffleWriteMetrics = None

    def __post_init__(self):
        if self.input_metrics:
            self.input_metrics = InputMetrics(self.input_metrics)
        if self.output_metrics:
            self.output_metrics = OutputMetrics(self.output_metrics)
        if self.shuffle_read_metrics:
            self.shuffle_read_metrics = ShuffleReadMetrics(self.shuffle_read_metrics)
        if self.shuffle_write_metrics:
            self.shuffle_write_metrics = ShuffleWriteMetrics(self.shuffle_write_metrics)


@dataclass
class Task(BaseSparkModel):
    accumulator_updates: int = None  # []
    attempt: int = None  # 0
    duration: int = None  # 11
    executor_id: str = None  # "driver"
    executor_logs: Dict = field(default_factory=dict)  # {}
    getting_result_time: int = None  # 0
    host: str = None  # "fecb8bf9abfc"
    index: int = None  # 0
    launch_time: str = None  # "2023-10-15T10:17:00.761GMT"
    partition_id: int = None  # 0
    scheduler_delay: int = None  # 3
    speculative: bool = None  # false
    status: TaskStatus = None  # "SUCCESS"
    task_id: int = None  # 54
    task_locality: Locality = None  # "NODE_LOCAL"
    task_metrics: TaskMetrics = None  # {}

    def __post_init__(self):
        if self.status:
            self.status = TaskStatus(self.status)

        if self.task_locality:
            self.task_locality = Locality(self.task_locality)

        if self.task_metrics:
            self.task_metrics = TaskMetrics(self.task_metrics)


@dataclass
class Stage(BaseSparkModel):
    accumulator_updates: List[str] = field(default_factory=list)  # []
    attempt_id: int = None  # 0
    completion_time: str = None  # "2023-10-15T10:17:00.772GMT"
    # org.apache.spark.sql.Dataset.count(Dataset.scala:3625)
    # java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    # java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke
    #   (NativeMethodAccessorImpl.java:62)
    # java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke
    #   (DelegatingMethodAccessorImpl.java:43)
    # java.base/java.lang.reflect.Method.invoke(Method.java:566)
    # py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
    # py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
    # py4j.Gateway.invoke(Gateway.java:282)
    # py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
    # py4j.commands.CallCommand.execute(CallCommand.java:79)
    # py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
    # py4j.ClientServerConnection.run(ClientServerConnection.java:106)
    # java.base/java.lang.Thread.run(Thread.java:829)
    details: str = None
    disk_bytes_spilled: int = None   # 0
    executor_cpu_time: int = None   # 1442666
    executor_deserialize_cpu_time: int = None  # 988667
    executor_deserialize_time: int = None  # 0
    executor_run_time: int = None  # 8
    first_task_launched_time: str = None  # "2023-10-15T10:17:00.761GMT"
    input_bytes: int = None  # 0
    input_records: int = None  # 0
    is_shuffle_push_enabled: bool = None  # false
    jvm_gc_time: int = None  # 0
    killed_tasks_summary: Dict = field(default_factory=dict)  # {}
    memory_bytes_spilled: int = None  # 0
    name: str = None  # "count at NativeMethodAccessorImpl.java:0"
    num_active_tasks: int = None  # 0
    num_complete_tasks: int = None  # 1
    num_completed_indices: int = None  # 1
    num_failed_tasks: int = None  # 0
    num_killed_tasks: int = None  # 0
    num_tasks: int = None  # 1
    output_bytes: int = None  # 0
    output_records: int = None  # 0
    peak_execution_memory: int = None  # 0
    peak_executor_metrics: Metrics = None  # {}
    rdd_ids: List[int] = None  # [227, 225, 226]
    resource_profile_id: int = None  # 0
    result_serialization_time: int = None  # 0
    result_size: int = None  # 3952
    scheduling_pool: str = None  # "default"
    shuffle_corrupt_merged_block_chunks: int = None  # 0
    shuffle_fetch_wait_time: int = None  # 0
    shuffle_local_blocks_fetched: int = None  # 1
    shuffle_local_bytes_read: int = None  # 59
    shuffle_merged_fetch_fallback_count: int = None  # 0
    shuffle_merged_local_blocks_fetched: int = None  # 0
    shuffle_merged_local_bytes_read: int = None  # 0
    shuffle_merged_local_chunks_fetched: int = None  # 0
    shuffle_merged_remote_blocks_fetched: int = None  # 0
    shuffle_merged_remote_bytes_read: int = None  # 0
    shuffle_merged_remote_chunks_fetched: int = None  # 0
    shuffle_merged_remote_reqs_duration: int = None  # 0
    shuffle_mergers_count: int = None  # 0
    shuffle_read_bytes: int = None  # 59
    shuffle_read_records: int = None  # 1
    shuffle_remote_blocks_fetched: int = None  # 0
    shuffle_remote_bytes_read: int = None  # 0
    shuffle_remote_bytes_read_to_disk: int = None  # 0
    shuffle_remote_reqs_duration: int = None  # 0
    shuffle_write_bytes: int = None  # 0
    shuffle_write_records: int = None  # 0
    shuffle_write_time: int = None  # 0
    stage_id: int = None  # 82
    status: StageStatus = None  # "COMPLETE"
    submission_time: str = None  # "2023-10-15T10:17:00.759GMT"

    def __post_init__(self):
        if self.peak_executor_metrics:
            self.peak_executor_metrics = Metrics.load(**self.peak_executor_metrics)

        if self.status:
            self.status = StageStatus(self.status)

    @property
    def id(self) -> int:
        return self.stage_id


@dataclass
class StageAttempt(Stage):
    accumulator_updates: List[str] = field(default_factory=list)  # []
    attempt_id: int = None  # 0
    completion_time: str = None  # "2023-10-15T10:17:00.772GMT"
    # org.apache.spark.sql.Dataset.count(Dataset.scala:3625)
    # java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    # java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke
    #   (NativeMethodAccessorImpl.java:62)
    # java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke
    #   (DelegatingMethodAccessorImpl.java:43)
    # java.base/java.lang.reflect.Method.invoke(Method.java:566)
    # py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
    # py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
    # py4j.Gateway.invoke(Gateway.java:282)
    # py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
    # py4j.commands.CallCommand.execute(CallCommand.java:79)
    # py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
    # py4j.ClientServerConnection.run(ClientServerConnection.java:106)
    # java.base/java.lang.Thread.run(Thread.java:829)"
    details: str = None
    disk_bytes_spilled: int = None  # 0
    executor_cpu_time: int = None  # 1442666
    executor_deserialize_cpu_time: int = None  # 988667
    executor_deserialize_time: int = None  # 0
    executor_run_time: int = None  # 8
    executor_summary: ExecutorSummary = None  # {}
    first_task_launched_time: str = None  # "2023-10-15T10:17:00.761GMT"
    input_bytes: int = None  # 0
    input_records: int = None  # 0
    is_shuffle_push_enabled: bool = None  # false
    jvm_gc_time: int = None  # 0
    killed_tasks_summary: Dict = field(default_factory=dict)  # {}
    memory_bytes_spilled: int = None  # 0
    name: str = None  # "count at NativeMethodAccessorImpl.java:0"
    num_active_tasks: int = None  # 0
    num_complete_tasks: int = None  # 1
    num_completed_indices: int = None  # 1
    num_failed_tasks: int = None  # 0
    num_killed_tasks: int = None  # 0
    num_tasks: int = None  # 1
    output_bytes: int = None  # 0
    output_records: int = None  # 0
    peak_execution_memory: int = None  # 0
    peak_executor_metrics: Metrics = None  # {}
    rdd_ids: List[int] = None  # [227, 225, 226]
    resource_profile_id: int = None  # 0
    result_serialization_time: int = None  # 0
    result_size: int = None  # 3952
    scheduling_pool: str = None  # "default"
    shuffle_corrupt_merged_block_chunks: int = None  # 0
    shuffle_fetch_wait_time: int = None  # 0
    shuffle_local_blocks_fetched: int = None  # 1
    shuffle_local_bytes_read: int = None  # 59
    shuffle_merged_fetch_fallback_count: int = None  # 0
    shuffle_merged_local_blocks_fetched: int = None  # 0
    shuffle_merged_local_bytes_read: int = None  # 0
    shuffle_merged_local_chunks_fetched: int = None  # 0
    shuffle_merged_remote_blocks_fetched: int = None  # 0
    shuffle_merged_remote_bytes_read: int = None  # 0
    shuffle_merged_remote_chunks_fetched: int = None  # 0
    shuffle_merged_remote_reqs_duration: int = None  # 0
    shuffle_mergers_count: int = None  # 0
    shuffle_read_bytes: int = None  # 59
    shuffle_read_records: int = None  # 1
    shuffle_remote_blocks_fetched: int = None  # 0
    shuffle_remote_bytes_read: int = None  # 0
    shuffle_remote_bytes_read_to_disk: int = None  # 0
    shuffle_remote_reqs_duration: int = None  # 0
    shuffle_write_bytes: int = None  # 0
    shuffle_write_records: int = None  # 0
    shuffle_write_time: int = None  # 0
    stage_id: int = None  # 82
    status: StageStatus = None  # "COMPLETE"
    submission_time: str = None  # "2023-10-15T10:17:00.759GMT"
    tasks: Dict = field(default_factory=dict)  # {}

    def __post_init__(self):
        super().__post_init__()

        if self.executor_summary:
            self.executor_summary = ExecutorSummary.load(**self.executor_summary)

        if self.tasks:
            tasks = {}
            for k, v in self.tasks.items():
                tasks[k] = Task.load(**v)
            self.tasks = tasks

    @property
    def id(self) -> int:
        return self.attempt_id
