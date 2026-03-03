from ld_client import ld_service, Context


import time
import random



def get_recommendations(user_group: str):
    context = Context.builder(f'user-{user_group}').set('group', user_group).build()
    
    is_premium, reason = ld_service.get_flag("use-complex-algorithm", context)
    
    if is_premium:
        items = ["Premium AI Item", "High-Tech Gadget"]
    else:
        items = ["Standard Item A", "Standard Item B"]
    
    chance = 0.8 if is_premium else 0.2
    if random.random() < chance:
        ld_service.track_event("recommendation-click", context)
        clicked = True
    else:
        clicked = False

    return items, reason, clicked

if __name__ == "__main__":
    groups = ["beta-testers", "standard-users"]
    
    print(" Starting Advanced LD Demo.....")
    for group in groups:
        items, reason, clicked = get_recommendations(group)
        print(f"\nGroup: {group}")
        print(f"Match Reason: {reason}")
        print(f"Items Served: {items}")
        print(f"User Clicked: {'YES' if clicked else 'NO'}")
    
    ld_service.close()
