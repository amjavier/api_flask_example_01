import os
from waitress import serve
import my_app

# retrieve port
def get_port():
  return int(os.environ.get("PORT", 8080))

serve(my_app.app, host='0.0.0.0', port=get_port()) # port=8080