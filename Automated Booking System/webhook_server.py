from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from booking_system import BookingSystem
from urllib.parse import parse_qs, urlparse

class WebhookHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.booking_system = BookingSystem()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        response_data = {}
        
        if path == '/webhook/booking':
            # Handle Zapier webhook for new booking
            try:
                booking = self.booking_system.create_booking(
                    data['customer_name'],
                    data['service'],
                    data['date']
                )
                response_data = {'status': 'success', 'booking': booking}
                self.send_response(200)
            except Exception as e:
                response_data = {'status': 'error', 'message': str(e)}
                self.send_response(400)
                
        elif path == '/api/bookings':
            # RPA API endpoint for creating bookings
            try:
                booking = self.booking_system.create_booking(
                    data['customer_name'],
                    data['service'],
                    data['date']
                )
                response_data = {'status': 'success', 'booking': booking}
                self.send_response(200)
            except Exception as e:
                response_data = {'status': 'error', 'message': str(e)}
                self.send_response(400)
        
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        response_data = {}
        
        if path == '/api/bookings':
            # RPA API endpoint for retrieving bookings
            response_data = {
                'status': 'success',
                'bookings': self.booking_system.bookings
            }
            self.send_response(200)
        else:
            response_data = {
                'status': 'error',
                'message': 'Endpoint not found'
            }
            self.send_response(404)
        
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))