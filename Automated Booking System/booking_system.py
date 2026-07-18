import json
from datetime import datetime
import os

class BookingSystem:
    def __init__(self):
        self.bookings = []
        self.load_bookings()

    def load_bookings(self):
        if os.path.exists('bookings.json'):
            try:
                with open('bookings.json', 'r') as f:
                    self.bookings = json.load(f)
            except:
                self.bookings = []

    def save_bookings(self):
        with open('bookings.json', 'w') as f:
            json.dump(self.bookings, f, indent=2)

    def create_booking(self, customer_name, service, date):
        booking = {
            'id': len(self.bookings) + 1,
            'customer_name': customer_name,
            'service': service,
            'date': date,
            'status': 'confirmed',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.bookings.append(booking)
        self.save_bookings()
        self.send_confirmation(booking)
        self.update_crm(booking)
        return booking

    def send_confirmation(self, booking):
        # Simulate sending email confirmation
        confirmation = f"""
        === Booking Confirmation ===
        Dear {booking['customer_name']},
        
        Your booking has been confirmed!
        
        Details:
        - Service: {booking['service']}
        - Date: {booking['date']}
        - Booking ID: {booking['id']}
        
        Thank you for choosing our service!
        """
        print("\nSending confirmation email:")
        print(confirmation)

    def update_crm(self, booking):
        # Simulate CRM update
        print(f"\nUpdating CRM for booking ID {booking['id']}...")
        print(f"Customer {booking['customer_name']} added to CRM system")

    def generate_report(self):
        # Generate simple analytics report
        total_bookings = len(self.bookings)
        services = {}
        for booking in self.bookings:
            service = booking['service']
            services[service] = services.get(service, 0) + 1

        report = f"""
        === Booking Analytics Report ===
        Total Bookings: {total_bookings}
        
        Services Breakdown:
        {'-' * 20}"""
        
        for service, count in services.items():
            report += f"\n{service}: {count} bookings"
        
        return report