from webhook_server import WebhookHandler, HTTPServer

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f"Starting server on port {port}...")
    print("\nAPI Endpoints:")
    print("1. Zapier Webhook: POST /webhook/booking")
    print("2. RPA Endpoints:")
    print("   - GET /api/bookings")
    print("   - POST /api/bookings")
    print("\nExample curl commands:")
    print("""
    # Create a booking (Zapier Webhook):
    curl -X POST http://localhost:8000/webhook/booking \\
         -H "Content-Type: application/json" \\
         -d '{"customer_name": "John Doe", "service": "Consultation", "date": "2024-02-01"}'
    
    # Get all bookings (RPA):
    curl http://localhost:8000/api/bookings
    
    # Create a booking (RPA):
    curl -X POST http://localhost:8000/api/bookings \\
         -H "Content-Type: application/json" \\
         -d '{"customer_name": "Jane Smith", "service": "Workshop", "date": "2024-02-02"}'
    """)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()