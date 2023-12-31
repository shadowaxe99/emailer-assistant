from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import json
import pickle

# Initialize the Calendar API
def get_calendar_service():
    creds = None
    if creds and not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/calendar'])
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

# Fetch free time slots for the next two months
def fetch_free_time(calendar_service, email_address):
    now = datetime.utcnow()
    end_time = now + timedelta(days=20)

    # Fetch the free/busy information
    body = {
        "timeMin": now.isoformat() + 'Z',
        "timeMax": end_time.isoformat() + 'Z',
        "items": [{"id": email_address}]
    }
    free_busy_response = calendar_service.freebusy().query(body=body).execute()

    # Extract the busy times
    busy_times = free_busy_response['calendars'][email_address]['busy']

    # Calculate the free times based on the busy times
    free_slots = []
    prev_end_time = now
    for busy in busy_times:
        busy_start = datetime.fromisoformat(busy['start'][:-1])
        busy_end = datetime.fromisoformat(busy['end'][:-1])
        if busy_start != prev_end_time:
            free_slots.append((prev_end_time, busy_start))
        prev_end_time = busy_end

    if prev_end_time != end_time:
        free_slots.append((prev_end_time, end_time))

    # Group free slots by day and format them
    free_slots_by_day = {}
    for start, end in free_slots:
        day = start.strftime('%Y-%m-%d')
        time_range = f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}"
        if day in free_slots_by_day:
            free_slots_by_day[day].append(time_range)
        else:
            free_slots_by_day[day] = [time_range]

    # Convert the grouped free slots into a human-readable format
    formatted_free_slots = []
    for day, time_ranges in free_slots_by_day.items():
        formatted_day = datetime.fromisoformat(day).strftime('%A, %d %B %Y')
        formatted_time_ranges = ', '.join(time_ranges)
        formatted_free_slots.append(f"{formatted_day}: {formatted_time_ranges}")

    return '\n'.join(formatted_free_slots)


if __name__ == '__main__':
    with open('calendar_service.pkl', 'rb') as f:
            calendar_service = pickle.load(f)

    print(fetch_free_time(calendar_service, "shivammittal2124@gmail.com"))
