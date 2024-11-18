erDiagram
    USER {
        int id PK
        string first_name
        string last_name
        string email
        string password
        boolean is_admin
    }
    
    PLACE {
        int id PK
        string title
        string description
        float price
        float latitude
        float longitude
        int owner_id FK
    }
    
    REVIEW {
        int id PK
        string text
        int rating
        int user_id FK
        int place_id FK
    }
    
    AMENITY {
        int id PK
        string name
    }
    
    PLACE_AMENITY {
        int place_id FK
        int amenity_id FK
    }

    USER ||--o| PLACE: "owns"
    USER ||--o| REVIEW: "writes"
    PLACE ||--o| REVIEW: "has"
    PLACE ||--o| PLACE_AMENITY: "includes"
    AMENITY ||--o| PLACE_AMENITY: "available_in"