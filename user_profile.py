from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class UserProfile:
    # Basic info
    name: str
    age: int
    gender: str                # "male" | "female" | "other"
    weight: float              # in kg
    height: float              # in cm
    
    # Lifestyle & goals
    #activity_level: str        # "sedentary", "light", "moderate", "active", "very_active"
    #goal: str                  # "weight_loss", "maintenance", "muscle_gain"
    
    # Preferences
    diet_type: Optional[str] = None   # "vegan", "vegetarian", "keto", "halal", etc.
    allergies: List[str] = field(default_factory=list)  
    disliked_foods: List[str] = field(default_factory=list)  
    
    # Location-based context
    country: Optional[str] = None     # e.g., "Belgium", "India", "USA"
    region: Optional[str] = None      # e.g., "Europe", "South Asia"
    
    # Calculated attributes
    daily_calories: Optional[float] = None
    protein_target: Optional[float] = None
    carb_target: Optional[float] = None
    fat_target: Optional[float] = None
