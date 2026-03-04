from ld_client import ld_service, Context
import random
import logging

logger = logging.getLogger(__name__)
FLAG_REC_ALGO = "use-complex-algorithm"
EVENT_REC_CLICK = "recommendation-click"


def get_recommendations(user_group: str) -> tuple:
    context = Context.builder(f'user-{user_group}').set('group', user_group).build()
    
    is_premium, reason = ld_service.get_flag(FLAG_REC_ALGO, context)
    
    items = ["Premium AI Item", "High-Tech Gadget"] if is_premium else ["Standard Item A", "Standard Item B"]
    
    chance = 0.8 if is_premium else 0.2
    clicked = random.random() < chance
    
    if clicked:
        ld_service.track_event(EVENT_REC_CLICK, context)

    return items, reason, clicked


if __name__ == "__main__":
    test_groups = ["beta-testers", "standard-users"]
    
    print("\n--- Starting Advanced LD Demo ---")
    
    for group in test_groups:
        items, reason, clicked = get_recommendations(group)
        
        print(f"\nGroup: {group}")
        print(f"Match Reason: {reason}")
        print(f"Items Served: {items}")
        print(f"User Clicked: {'YES' if clicked else 'NO'}")
    
    print("\n--- Demo Complete ---\n")
    ld_service.close()
