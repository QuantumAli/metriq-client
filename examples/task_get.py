from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.task_get("6102f848ff8f28281ae4ea4f")
assert result is not None
