from booking_system import BookingSystem

def simulate_integrations():
    """Simulate Zapier and RPA integrations"""
    system = BookingSystem()
    
    # Simulate Zapier webhook trigger
    print("\n=== Simulating Zapier Webhook Trigger ===")
    zapier_booking = system.create_booking(
        "Alice Cooper", 
        "Workshop", 
        "2024-02-01"
    )
    print("Zapier webhook would trigger actions in:")
    print("1. Google Calendar - Create event")
    print("2. Slack - Send notification")
    print("3. Mailchimp - Add to email campaign")
    
    # Simulate RPA interaction
    print("\n=== Simulating RPA Integration ===")
    print("RPA bot would:")
    print("1. Read bookings from system")
    print("2. Update legacy systems")
    print("3. Generate reports")
    
    # Generate and display report
    print("\n" + system.generate_report())

if __name__ == "__main__":
    simulate_integrations()