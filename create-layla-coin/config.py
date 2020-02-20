# Modify this file as you run through the tutorial

creator_address = ""
creator_passphrase = ""
receiver_address = ""
receiver_passphrase = ""

# Credentials to connect through an algod client
algod_address = ""
algod_token = ""

# Details of the asset creation transaction
asset_details = {
	"sender": creator_address,
	"asset_name": "LaylaGyozaCoin",
	"unit_name": "Woof",
	"total": 888888888,
	"decimals": 3,
	"default_frozen": False,
	"manager": creator_address,
	"reserve": creator_address,
	"freeze": creator_address,
	"clawback": creator_address,
	"url": "LaylaGyoza.jpg",
	"metadata_hash": b'O\x88\xfd\xf2\xd1\xfe\xee\x96+\xf9\xf0\xb6\xb2\x8d\r\xb5\xced)#\x9bV\xce\xa4\x81\xa6\xb9\xbd\x0e\xf7al'
}

metadata_file = "LaylaGyoza.jpg"
metadatahash_b64 = "T4j98tH+7pYr+fC2so0Ntc5kKSObVs6kgaa5vQ73YWw="

# The asset ID is available after the asset is created.
asset_id = 191674