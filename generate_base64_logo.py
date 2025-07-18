#!/usr/bin/env python3
"""
Generate base64 data URL for the SumHealth logo
"""

import base64

def generate_logo_data_url():
    """Generate base64 data URL for the logo image."""
    try:
        with open('assets/sumnew.png', 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            data_url = f'data:image/png;base64,{encoded}'
            
        with open('logo_data_url.txt', 'w') as out:
            out.write(data_url)
            
        print("✅ Base64 data URL generated successfully!")
        print(f"Length: {len(data_url)} characters")
        print(f"Preview: {data_url[:100]}...")
        
        return data_url
        
    except Exception as e:
        print(f"❌ Error generating base64 data URL: {e}")
        return None

if __name__ == "__main__":
    generate_logo_data_url()
