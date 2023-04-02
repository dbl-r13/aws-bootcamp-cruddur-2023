from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging
# from lib.db import pool, query_wrap_array
from lib.db import db

LOGGER = logging.getLogger(__name__)

tracer = trace.get_tracer("home_activities")

class HomeActivities:
  def run(cognito_user_id=None):
    LOGGER.info('Hello Cloudwatch! from  /api/activities/home')
    with tracer.start_as_current_span("homeActivitiesMockedData"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()

      span.set_attribute("app.now", now.isoformat())
    results = db.query_array_json("""
    SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
    """)
    return results
  