from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone, timedelta

from app.database import SessionLocal
from app.models.eventModel import Event
from app.models.ticketModel import Ticket

scheduler = BackgroundScheduler()

def update_event_status():
    db = SessionLocal()
    try:
        now = datetime.now(timezone.utc)

        db.query(Event).filter(
            Event.status == 'active',
            Event.eventDate <= now
        ).update(
            {'status':'in_progress'},
            synchronize_session=False
        )

        finished_events = (db.query(Event).filter(
            Event.status == 'in_progress',
            Event.eventDate + timedelta(hours=24) <= now
        ).all())

        finished_events_ids = [e.id for e in finished_events]

        if finished_events_ids:
            db.query(Event).filter(
                Event.id.in_(finished_events_ids)
            ).update(
                {'status': 'finished'},
                synchronize_session=False
            )

            db.query(Ticket).filter(
                Ticket.event_id.in_(finished_events_ids),
                Ticket.status == 'active'
            ).update(
                {'status':'finished'},
                synchronize_session=False
            )

        db.commit()
    finally:
        db.close()

def start_cheduler():
    scheduler.add_job(
        update_event_status,
        trigger='interval',
        minutes=1,
        id='update_event_status',
        replace_existing=True
    )
    scheduler.start()