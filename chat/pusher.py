import pusher
from .config import APP_ID,KEY,SECRET,CLUSTER

pusher_client = pusher.Pusher(
  app_id= APP_ID,
  key= KEY,
  secret= SECRET,
  cluster= CLUSTER,
  ssl=True
)

