from aioca import caget
from fixtures.mocked_panda import TEST_PREFIX


def test_conftest_loads_fixtures_from_other_files(table_fields):
    "Tests that the `panda_data.py` fixtures are being loaded"
    ...


async def test_fake_panda_and_ioc(mocked_panda_standard_responses):
    """Tests that the test ioc launches and the PVs are broadcasted"""
    tmp_path, child_conn, responses, command_queue = mocked_panda_standard_responses

    # PVs are broadcast
    gate_delay = await caget(f"{TEST_PREFIX}:PCAP1:GATE:DELAY")
    assert gate_delay == 1
