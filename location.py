import gps
from communication import CommunicationManager
import json

class LocationManager:
    
    @classmethod
    def send_gps_location(cls):
        session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        CommunicationManager.start_location_server()
        try:
            while True:
                report = session.next()
                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and hasattr(report, 'lon'):
                        latitude = report.lat
                        longitude = report.lon
                        data = {'longitude': longitude, 'latitude': latitude}
                        message = json.dumps(data)
                        CommunicationManager.send_location_data(message)
        except KeyboardInterrupt:
            print("Exiting GPS script.")
