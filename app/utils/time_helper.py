# %%
# import modules
from datetime import datetime, UTC


# %%
# define function
def format_seconds_since_epoch_to_iso(seconds_since_epoch: float) -> str:
    return datetime.fromtimestamp(
        timestamp=seconds_since_epoch,
        tz=UTC
    ).isoformat()


# %%
