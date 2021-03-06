"""
Constants used by the clean_address() and validate_address() functions
"""

TAG_MAPPING = {
    "OccupancyType": "apartment",
    "OccupancyIdentifier": "apartment",
    "SubaddressType": "apartment",
    "SubaddressIdentifier": "apartment",
    "BuildingName": "building",
    "AddressNumber": "house_number",
    "StreetNamePreDirectional": "street_prefix",
    "StreetName": "street_name",
    "StreetNamePostType": "street_suffix",
    "PlaceName": "city",
    "StateName": "state",
    "ZipCode": "zipcode",
}

KEYWORDS = [
    "house_number",
    "street_prefix_abbr",
    "street_prefix_full",
    "street_name",
    "street_suffix_abbr",
    "street_suffix_full",
    "city",
    "state_abbr",
    "state_full",
    "zipcode",
    "building",
    "apartment",
]

PREFIXES = {
    "n": "N.",
    "e": "E.",
    "s": "S.",
    "w": "W.",
    "ne": "NE.",
    "nw": "NW.",
    "se": "SE.",
    "sw": "SW.",
    "north": "N.",
    "east": "E.",
    "south": "S.",
    "west": "W.",
    "northeast": "NE.",
    "northwest": "NW.",
    "southeast": "SE.",
    "southwest": "SW.",
}

FULL_PREFIX = {
    "N.": "North",
    "E.": "East",
    "S.": "South",
    "W.": "West",
    "NE.": "North East",
    "NW.": "North West",
    "SE.": "South East",
    "SW.": "South West",
}

FULL_STATES = {
    "Mississippi": "MS",
    "Oklahoma": "OK",
    "Delaware": "DE",
    "Minnesota": "MN",
    "Illinois": "IL",
    "Arkansas": "AR",
    "New Mexico": "NM",
    "Indiana": "IN",
    "Maryland": "MD",
    "Louisiana": "LA",
    "Idaho": "ID",
    "Wyoming": "WY",
    "Tennessee": "TN",
    "Arizona": "AZ",
    "Iowa": "IA",
    "Michigan": "MI",
    "Kansas": "KS",
    "Utah": "UT",
    "Virginia": "VA",
    "Oregon": "OR",
    "Connecticut": "CT",
    "Montana": "MT",
    "California": "CA",
    "Massachusetts": "MA",
    "West Virginia": "WV",
    "South Carolina": "SC",
    "New Hampshire": "NH",
    "Wisconsin": "WI",
    "Vermont": "VT",
    "Georgia": "GA",
    "North Dakota": "ND",
    "Pennsylvania": "PA",
    "Florida": "FL",
    "Alaska": "AK",
    "Kentucky": "KY",
    "Hawaii": "HI",
    "Nebraska": "NE",
    "Missouri": "MO",
    "Ohio": "OH",
    "Alabama": "AL",
    "New York": "NY",
    "South Dakota": "SD",
    "Colorado": "CO",
    "New Jersey": "NJ",
    "Washington": "WA",
    "North Carolina": "NC",
    "District of Columbia": "DC",
    "Texas": "TX",
    "Nevada": "NV",
    "Maine": "ME",
    "Rhode Island": "RI",
}

ABBR_STATES = {state_abbr: state_full for state_full, state_abbr in FULL_STATES.items()}

SUFFIXES = {
    "ALLEE": ("ALY", "ALLEY"),
    "ALLEY": ("ALY", "ALLEY"),
    "ALLY": ("ALY", "ALLEY"),
    "ALY": ("ALY", "ALLEY"),
    "ANEX": ("ANX", "ANEX"),
    "ANNEX": ("ANX", "ANEX"),
    "ANNX": ("ANX", "ANEX"),
    "ANX": ("ANX", "ANEX"),
    "ARC": ("ARC", "ARCADE"),
    "ARCADE": ("ARC", "ARCADE"),
    "AV": ("AVE", "AVENUE"),
    "AVE": ("AVE", "AVENUE"),
    "AVEN": ("AVE", "AVENUE"),
    "AVENU": ("AVE", "AVENUE"),
    "AVENUE": ("AVE", "AVENUE"),
    "AVN": ("AVE", "AVENUE"),
    "AVNUE": ("AVE", "AVENUE"),
    "BAYOO": ("BYU", "BAYOU"),
    "BAYOU": ("BYU", "BAYOU"),
    "BCH": ("BCH", "BEACH"),
    "BEACH": ("BCH", "BEACH"),
    "BEND": ("BND", "BEND"),
    "BND": ("BND", "BEND"),
    "BLF": ("BLF", "BLUFF"),
    "BLUF": ("BLF", "BLUFF"),
    "BLUFF": ("BLF", "BLUFF"),
    "BLUFFS": ("BLFS", "BLUFFS"),
    "BOT": ("BTM", "BOTTOM"),
    "BOTTM": ("BTM", "BOTTOM"),
    "BOTTOM": ("BTM", "BOTTOM"),
    "BTM": ("BTM", "BOTTOM"),
    "BLVD": ("BLVD", "BOULEVARD"),
    "BOUL": ("BLVD", "BOULEVARD"),
    "BOULEVARD": ("BLVD", "BOULEVARD"),
    "BOULV": ("BLVD", "BOULEVARD"),
    "BR": ("BR", "BRANCH"),
    "BRANCH": ("BR", "BRANCH"),
    "BRNCH": ("BR", "BRANCH"),
    "BRDGE": ("BRG", "BRIDGE"),
    "BRG": ("BRG", "BRIDGE"),
    "BRIDGE": ("BRG", "BRIDGE"),
    "BRK": ("BRK", "BROOK"),
    "BROOK": ("BRK", "BROOK"),
    "BROOKS": ("BRKS", "BROOKS"),
    "BURG": ("BG", "BURG"),
    "BURGS": ("BGS", "BURGS"),
    "BYP": ("BYP", "BYPASS"),
    "BYPA": ("BYP", "BYPASS"),
    "BYPAS": ("BYP", "BYPASS"),
    "BYPASS": ("BYP", "BYPASS"),
    "BYPS": ("BYP", "BYPASS"),
    "CAMP": ("CP", "CAMP"),
    "CMP": ("CP", "CAMP"),
    "CP": ("CP", "CAMP"),
    "CANYN": ("CYN", "CANYON"),
    "CANYON": ("CYN", "CANYON"),
    "CNYN": ("CYN", "CANYON"),
    "CYN": ("CYN", "CANYON"),
    "CAPE": ("CPE", "CAPE"),
    "CPE": ("CPE", "CAPE"),
    "CAUSEWAY": ("CSWY", "CAUSEWAY"),
    "CAUSWAY": ("CSWY", "CAUSEWAY"),
    "CSWY": ("CSWY", "CAUSEWAY"),
    "CEN": ("CTR", "CENTER"),
    "CENT": ("CTR", "CENTER"),
    "CENTER": ("CTR", "CENTER"),
    "CENTR": ("CTR", "CENTER"),
    "CENTRE": ("CTR", "CENTER"),
    "CNTER": ("CTR", "CENTER"),
    "CNTR": ("CTR", "CENTER"),
    "CTR": ("CTR", "CENTER"),
    "CENTERS": ("CTRS", "CENTERS"),
    "CIR": ("CIR", "CIRCLE"),
    "CIRC": ("CIR", "CIRCLE"),
    "CIRCL": ("CIR", "CIRCLE"),
    "CIRCLE": ("CIR", "CIRCLE"),
    "CRCL": ("CIR", "CIRCLE"),
    "CRCLE": ("CIR", "CIRCLE"),
    "CIRCLES": ("CIR", "CIRCLES"),
    "CLF": ("CLF", "CLIFF"),
    "CLIFF": ("CLF", "CLIFF"),
    "CLFS": ("CLFS", "CLIFFS"),
    "CLIFFS": ("CLFS", "CLIFFS"),
    "CLB": ("CLB", "CLUB"),
    "CLUB": ("CLB", "CLUB"),
    "COMMON": ("CMN", "COMMON"),
    "COR": ("COR", "CORNER"),
    "CORNER": ("COR", "CORNER"),
    "CORNERS": ("CORS", "CORNERS"),
    "CORS": ("CORS", "CORNERS"),
    "COURSE": ("CRSE", "COURSE"),
    "CRSE": ("CRSE", "COURSE"),
    "COURT": ("CT", "COURT"),
    "CRT": ("CT", "COURT"),
    "CT": ("CT", "COURT"),
    "COURTS": ("CTS", "COURTS"),
    "COVE": ("CV", "COVE"),
    "CV": ("CV", "COVE"),
    "COVES": ("CVS", "COVES"),
    "CK": ("CRK", "CREEK"),
    "CR": ("CRK", "CREEK"),
    "CREEK": ("CRK", "CREEK"),
    "CRK": ("CRK", "CREEK"),
    "CRECENT": ("CRES", "CRESCENT"),
    "CRES": ("CRES", "CRESCENT"),
    "CRESCENT": ("CRES", "CRESCENT"),
    "CRESENT": ("CRES", "CRESCENT"),
    "CRSCNT": ("CRES", "CRESCENT"),
    "CRSENT": ("CRES", "CRESCENT"),
    "CRSNT": ("CRES", "CRESCENT"),
    "CREST": ("CREST", "CREST"),
    "CROSSING": ("XING", "CROSSING"),
    "CRSSING": ("XING", "CROSSING"),
    "CRSSNG": ("XING", "CROSSING"),
    "XING": ("XING", "CROSSING"),
    "CROSSROAD": ("XRD", "CROSSROAD"),
    "CURVE": ("CURV", "CURVE"),
    "DALE": ("DL", "DALE"),
    "DL": ("DL", "DALE"),
    "DAM": ("DM", "DAM"),
    "DM": ("DM", "DAM"),
    "DIV": ("DV", "DIVIDE"),
    "DIVIDE": ("DV", "DIVIDE"),
    "DV": ("DV", "DIVIDE"),
    "DVD": ("DV", "DIVIDE"),
    "DR": ("DR", "DRIVE"),
    "DRIV": ("DR", "DRIVE"),
    "DRIVE": ("DR", "DRIVE"),
    "DRV": ("DR", "DRIVE"),
    "DRIVES": ("DRS", "DRIVES"),
    "EST": ("EST", "ESTATE"),
    "ESTATE": ("EST", "ESTATE"),
    "ESTATES": ("ESTS", "ESTATES"),
    "ESTS": ("ESTS", "ESTATES"),
    "EXP": ("EXPY", "EXPRESSWAY"),
    "EXPR": ("EXPY", "EXPRESSWAY"),
    "EXPRESS": ("EXPY", "EXPRESSWAY"),
    "EXPRESSWAY": ("EXPY", "EXPRESSWAY"),
    "EXPW": ("EXPY", "EXPRESSWAY"),
    "EXPY": ("EXPY", "EXPRESSWAY"),
    "EXT": ("EXT", "EXTENSION"),
    "EXTENSION": ("EXT", "EXTENSION"),
    "EXTN": ("EXT", "EXTENSION"),
    "EXTNSN": ("EXT", "EXTENSION"),
    "EXTENSIONS": ("EXTS", "EXTENSIONS"),
    "EXTS": ("EXTS", "EXTENSIONS"),
    "FALL": ("FALL", "FALL"),
    "FALLS": ("FLS", "FALLS"),
    "FLS": ("FLS", "FALLS"),
    "FERRY": ("FRY", "FERRY"),
    "FRRY": ("FRY", "FERRY"),
    "FRY": ("FRY", "FERRY"),
    "FIELD": ("FLD", "FIELD"),
    "FLD": ("FLD", "FIELD"),
    "FIELDS": ("FLDS", "FIELDS"),
    "FLDS": ("FLDS", "FIELDS"),
    "FLAT": ("FLT", "FLAT"),
    "FLT": ("FLT", "FLAT"),
    "FLATS": ("FLTS", "FLATS"),
    "FLTS": ("FLTS", "FLATS"),
    "FORD": ("FRD", "FORD"),
    "FRD": ("FRD", "FORD"),
    "FORDS": ("FRDS", "FORDS"),
    "FOREST": ("FRST", "FOREST"),
    "FORESTS": ("FRST", "FOREST"),
    "FRST": ("FRST", "FOREST"),
    "FORG": ("FRG", "FORGE"),
    "FORGE": ("FRG", "FORGE"),
    "FRG": ("FRG", "FORGE"),
    "FORGES": ("FRGS", "FORGES"),
    "FORK": ("FRK", "FORK"),
    "FRK": ("FRK", "FORK"),
    "FORKS": ("FRKS", "FORKS"),
    "FRKS": ("FRKS", "FORKS"),
    "FORT": ("FT", "FORT"),
    "FRT": ("FT", "FORT"),
    "FT": ("FT", "FORT"),
    "FREEWAY": ("FWY", "FREEWAY"),
    "FREEWY": ("FWY", "FREEWAY"),
    "FRWAY": ("FWY", "FREEWAY"),
    "FRWY": ("FWY", "FREEWAY"),
    "FWY": ("FWY", "FREEWAY"),
    "GARDEN": ("GDN", "GARDEN"),
    "GARDN": ("GDN", "GARDEN"),
    "GDN": ("GDN", "GARDEN"),
    "GRDEN": ("GDN", "GARDEN"),
    "GRDN": ("GDN", "GARDEN"),
    "GARDENS": ("GDNS", "GARDENS"),
    "GDNS": ("GDNS", "GARDENS"),
    "GRDNS": ("GDNS", "GARDENS"),
    "GATEWAY": ("GTWY", "GATEWAY"),
    "GATEWY": ("GTWY", "GATEWAY"),
    "GATWAY": ("GTWY", "GATEWAY"),
    "GTWAY": ("GTWY", "GATEWAY"),
    "GTWY": ("GTWY", "GATEWAY"),
    "GLEN": ("GLN", "GLEN"),
    "GLN": ("GLN", "GLEN"),
    "GLENS": ("GLNS", "GLENS"),
    "GREEN": ("GRN", "GREEN"),
    "GRN": ("GRN", "GREEN"),
    "GREENS": ("GRNS", "GREENS"),
    "GROV": ("GRV", "GROVE"),
    "GROVE": ("GRV", "GROVE"),
    "GRV": ("GRV", "GROVE"),
    "GROVES": ("GRVS", "GROVES"),
    "HARB": ("HBR", "HARBOR"),
    "HARBOR": ("HBR", "HARBOR"),
    "HARBR": ("HBR", "HARBOR"),
    "HBR": ("HBR", "HARBOR"),
    "HRBOR": ("HBR", "HARBOR"),
    "HARBORS": ("HBRS", "HARBORS"),
    "HAVEN": ("HVN", "HAVEN"),
    "HAVN": ("HVN", "HAVEN"),
    "HVN": ("HVN", "HAVEN"),
    "HEIGHT": ("HTS", "HEIGHTS"),
    "HEIGHTS": ("HTS", "HEIGHTS"),
    "HGTS": ("HTS", "HEIGHTS"),
    "HT": ("HTS", "HEIGHTS"),
    "HTS": ("HTS", "HEIGHTS"),
    "HIGHWAY": ("HWY", "HIGHWAY"),
    "HIGHWY": ("HWY", "HIGHWAY"),
    "HIWAY": ("HWY", "HIGHWAY"),
    "HIWY": ("HWY", "HIGHWAY"),
    "HWAY": ("HWY", "HIGHWAY"),
    "HWY": ("HWY", "HIGHWAY"),
    "HILL": ("HL", "HILL"),
    "HL": ("HL", "HILL"),
    "HILLS": ("HLS", "HILLS"),
    "HLS": ("HLS", "HILLS"),
    "HLLW": ("HOLW", "HOLLOW"),
    "HOLLOW": ("HOLW", "HOLLOW"),
    "HOLLOWS": ("HOLW", "HOLLOW"),
    "HOLW": ("HOLW", "HOLLOW"),
    "HOLWS": ("HOLW", "HOLLOW"),
    "INLET": ("INLT", "INLET"),
    "INLT": ("INLT", "INLET"),
    "IS": ("IS", "ISLAND"),
    "ISLAND": ("IS", "ISLAND"),
    "ISLND": ("IS", "ISLAND"),
    "ISLANDS": ("ISS", "ISLANDS"),
    "ISLNDS": ("ISS", "ISLANDS"),
    "ISS": ("ISS", "ISLANDS"),
    "ISLE": ("ISLE", "ISLE"),
    "ISLES": ("ISLE", "ISLE"),
    "JCT": ("JCT", "JUNCTION"),
    "JCTION": ("JCT", "JUNCTION"),
    "JCTN": ("JCT", "JUNCTION"),
    "JUNCTION": ("JCT", "JUNCTION"),
    "JUNCTN": ("JCT", "JUNCTION"),
    "JUNCTON": ("JCT", "JUNCTION"),
    "JCTNS": ("JCTS", "JUNCTIONS"),
    "JCTS": ("JCTS", "JUNCTIONS"),
    "JUNCTIONS": ("JCTS", "JUNCTIONS"),
    "KEY": ("KY", "KEY"),
    "KY": ("KY", "KEY"),
    "KEYS": ("KYS", "KEYS"),
    "KYS": ("KYS", "KEYS"),
    "KNL": ("KNL", "KNOLL"),
    "KNOL": ("KNL", "KNOLL"),
    "KNOLL": ("KNL", "KNOLL"),
    "KNLS": ("KNLS", "KNOLLS"),
    "KNOLLS": ("KNLS", "KNOLLS"),
    "LAKE": ("LK", "LAKE"),
    "LK": ("LK", "LAKE"),
    "LAKES": ("LKS", "LAKES"),
    "LKS": ("LKS", "LAKES"),
    "LAND": ("LAND", "LAND"),
    "LANDING": ("LNDG", "LANDING"),
    "LNDG": ("LNDG", "LANDING"),
    "LNDNG": ("LNDG", "LANDING"),
    "LA": ("LN", "LANE"),
    "LANE": ("LN", "LANE"),
    "LANES": ("LN", "LANE"),
    "LN": ("LN", "LANE"),
    "LGT": ("LGT", "LIGHT"),
    "LIGHT": ("LGT", "LIGHT"),
    "LIGHTS": ("LGTS", "LIGHTS"),
    "LF": ("LF", "LOAF"),
    "LOAF": ("LF", "LOAF"),
    "LCK": ("LCK", "LOCK"),
    "LOCK": ("LCK", "LOCK"),
    "LCKS": ("LCKS", "LOCKS"),
    "LOCKS": ("LCKS", "LOCKS"),
    "LDG": ("LDG", "LODGE"),
    "LDGE": ("LDG", "LODGE"),
    "LODG": ("LDG", "LODGE"),
    "LODGE": ("LDG", "LODGE"),
    "LOOP": ("LOOP", "LOOP"),
    "LOOPS": ("LOOP", "LOOP"),
    "MALL": ("MALL", "MALL"),
    "MANOR": ("MNR", "MANOR"),
    "MNR": ("MNR", "MANOR"),
    "MANORS": ("MNRS", "MANORS"),
    "MNRS": ("MNRS", "MANORS"),
    "MDW": ("MDW", "MEADOW"),
    "MEADOW": ("MDW", "MEADOW"),
    "MDWS": ("MDWS", "MEADOWS"),
    "MEADOWS": ("MDWS", "MEADOWS"),
    "MEDOWS": ("MDWS", "MEADOWS"),
    "MEWS": ("MEWS", "MEWS"),
    "MILL": ("ML", "MILL"),
    "ML": ("ML", "MILL"),
    "MILLS": ("MLS", "MILLS"),
    "MLS": ("MLS", "MILLS"),
    "MISSION": ("MSN", "MISSION"),
    "MISSN": ("MSN", "MISSION"),
    "MSN": ("MSN", "MISSION"),
    "MSSN": ("MSN", "MISSION"),
    "MOTORWAY": ("MTWY", "MOTORWAY"),
    "MNT": ("MT", "MOUNT"),
    "MOUNT": ("MT", "MOUNT"),
    "MT": ("MT", "MOUNT"),
    "MNTAIN": ("MTN", "MOUNTAIN"),
    "MNTN": ("MTN", "MOUNTAIN"),
    "MOUNTAIN": ("MTN", "MOUNTAIN"),
    "MOUNTIN": ("MTN", "MOUNTAIN"),
    "MTIN": ("MTN", "MOUNTAIN"),
    "MTN": ("MTN", "MOUNTAIN"),
    "MNTNS": ("MTNS", "MOUNTAINS"),
    "MOUNTAINS": ("MTNS", "MOUNTAINS"),
    "NCK": ("NCK", "NECK"),
    "NECK": ("NCK", "NECK"),
    "ORCH": ("ORCH", "ORCHARD"),
    "ORCHARD": ("ORCH", "ORCHARD"),
    "ORCHRD": ("ORCH", "ORCHARD"),
    "OVAL": ("OVAL", "OVAL"),
    "OVL": ("OVAL", "OVAL"),
    "OVERPASS": ("OPAS", "OVERPASS"),
    "PARK": ("PARK", "PARK"),
    "PK": ("PARK", "PARK"),
    "PRK": ("PARK", "PARK"),
    "PARKS": ("PARK", "PARKS"),
    "PARKWAY": ("PKWY", "PARKWAY"),
    "PARKWY": ("PKWY", "PARKWAY"),
    "PKWAY": ("PKWY", "PARKWAY"),
    "PKWY": ("PKWY", "PARKWAY"),
    "PKY": ("PKWY", "PARKWAY"),
    "PARKWAYS": ("PKWY", "PARKWAY"),
    "PKWYS": ("PKWY", "PARKWAY"),
    "PASS": ("PASS", "PASS"),
    "PASSAGE": ("PSGE", "PASSAGE"),
    "PATH": ("PATH", "PATH"),
    "PATHS": ("PATH", "PATH"),
    "PIKE": ("PIKE", "PIKE"),
    "PIKES": ("PIKE", "PIKE"),
    "PINE": ("PNE", "PINE"),
    "PINES": ("PNES", "PINES"),
    "PNES": ("PNES", "PINES"),
    "PL": ("PL", "PLACE"),
    "PLACE": ("PL", "PLACE"),
    "PLAIN": ("PLN", "PLAIN"),
    "PLN": ("PLN", "PLAIN"),
    "PLAINES": ("PLNS", "PLAINS"),
    "PLAINS": ("PLNS", "PLAINS"),
    "PLNS": ("PLNS", "PLAINS"),
    "PLAZA": ("PLZ", "PLAZA"),
    "PLZ": ("PLZ", "PLAZA"),
    "PLZA": ("PLZ", "PLAZA"),
    "POINT": ("PT", "POINT"),
    "PT": ("PT", "POINT"),
    "POINTS": ("PTS", "POINTS"),
    "PTS": ("PTS", "POINTS"),
    "PORT": ("PRT", "PORT"),
    "PRT": ("PRT", "PORT"),
    "PORTS": ("PRTS", "PORTS"),
    "PRTS": ("PRTS", "PORTS"),
    "PR": ("PR", "PRAIRIE"),
    "PRAIRIE": ("PR", "PRAIRIE"),
    "PRARIE": ("PR", "PRAIRIE"),
    "PRR": ("PR", "PRAIRIE"),
    "RAD": ("RADL", "RADIAL"),
    "RADIAL": ("RADL", "RADIAL"),
    "RADIEL": ("RADL", "RADIAL"),
    "RADL": ("RADL", "RADIAL"),
    "RAMP": ("RAMP", "RAMP"),
    "RANCH": ("RNCH", "RANCH"),
    "RANCHES": ("RNCH", "RANCH"),
    "RNCH": ("RNCH", "RANCH"),
    "RNCHS": ("RNCH", "RANCH"),
    "RAPID": ("RPD", "RAPID"),
    "RPD": ("RPD", "RAPID"),
    "RAPIDS": ("RPDS", "RAPIDS"),
    "RPDS": ("RPDS", "RAPIDS"),
    "REST": ("RST", "REST"),
    "RST": ("RST", "REST"),
    "RDG": ("RDG", "RIDGE"),
    "RDGE": ("RDG", "RIDGE"),
    "RIDGE": ("RDG", "RIDGE"),
    "RDGS": ("RDGS", "RIDGES"),
    "RIDGES": ("RDGS", "RIDGES"),
    "RIV": ("RIV", "RIVER"),
    "RIVER": ("RIV", "RIVER"),
    "RIVR": ("RIV", "RIVER"),
    "RVR": ("RIV", "RIVER"),
    "RD": ("RD", "ROAD"),
    "ROAD": ("RD", "ROAD"),
    "RDS": ("RDS", "ROADS"),
    "ROADS": ("RDS", "ROADS"),
    "ROUTE": ("RTE", "ROUTE"),
    "ROW": ("ROW", "ROW"),
    "RUE": ("RUE", "RUE"),
    "RUN": ("RUN", "RUN"),
    "SHL": ("SHL", "SHOAL"),
    "SHOAL": ("SHL", "SHOAL"),
    "SHLS": ("SHLS", "SHOALS"),
    "SHOALS": ("SHLS", "SHOALS"),
    "SHOAR": ("SHR", "SHORE"),
    "SHORE": ("SHR", "SHORE"),
    "SHR": ("SHR", "SHORE"),
    "SHOARS": ("SHRS", "SHORES"),
    "SHORES": ("SHRS", "SHORES"),
    "SHRS": ("SHRS", "SHORES"),
    "SKYWAY": ("SKWY", "SKYWAY"),
    "SPG": ("SPG", "SPRING"),
    "SPNG": ("SPG", "SPRING"),
    "SPRING": ("SPG", "SPRING"),
    "SPRNG": ("SPG", "SPRING"),
    "SPGS": ("SPGS", "SPRINGS"),
    "SPNGS": ("SPGS", "SPRINGS"),
    "SPRINGS": ("SPGS", "SPRINGS"),
    "SPRNGS": ("SPGS", "SPRINGS"),
    "SPUR": ("SPUR", "SPUR"),
    "SPURS": ("SPUR", "SPUR"),
    "SQ": ("SQ", "SQUARE"),
    "SQR": ("SQ", "SQUARE"),
    "SQRE": ("SQ", "SQUARE"),
    "SQU": ("SQ", "SQUARE"),
    "SQUARE": ("SQ", "SQUARE"),
    "SQRS": ("SQS", "SQUARES"),
    "SQUARES": ("SQS", "SQUARES"),
    "STA": ("STA", "STATION"),
    "STATION": ("STA", "STATION"),
    "STATN": ("STA", "STATION"),
    "STN": ("STA", "STATION"),
    "STRA": ("STRA", "STRAVENUE"),
    "STRAV": ("STRA", "STRAVENUE"),
    "STRAVE": ("STRA", "STRAVENUE"),
    "STRAVEN": ("STRA", "STRAVENUE"),
    "STRAVENUE": ("STRA", "STRAVENUE"),
    "STRAVN": ("STRA", "STRAVENUE"),
    "STRVN": ("STRA", "STRAVENUE"),
    "STRVNUE": ("STRA", "STRAVENUE"),
    "STREAM": ("STRM", "STREAM"),
    "STREME": ("STRM", "STREAM"),
    "STRM": ("STRM", "STREAM"),
    "ST": ("ST", "STREET"),
    "STR": ("ST", "STREET"),
    "STREET": ("ST", "STREET"),
    "STRT": ("ST", "STREET"),
    "STREETS": ("STS", "STREETS"),
    "SMT": ("SMT", "SUMMIT"),
    "SUMIT": ("SMT", "SUMMIT"),
    "SUMITT": ("SMT", "SUMMIT"),
    "SUMMIT": ("SMT", "SUMMIT"),
    "TER": ("TER", "TERRACE"),
    "TERR": ("TER", "TERRACE"),
    "TERRACE": ("TER", "TERRACE"),
    "THROUGHWAY": ("TRWY", "THROUGHWAY"),
    "TRACE": ("TRCE", "TRACE"),
    "TRACES": ("TRCE", "TRACE"),
    "TRCE": ("TRCE", "TRACE"),
    "TRACK": ("TRAK", "TRACK"),
    "TRACKS": ("TRAK", "TRACK"),
    "TRAK": ("TRAK", "TRACK"),
    "TRK": ("TRAK", "TRACK"),
    "TRKS": ("TRAK", "TRACK"),
    "TRAFFICWAY": ("TRFY", "TRAFFICWAY"),
    "TRFY": ("TRFY", "TRAFFICWAY"),
    "TR": ("TRL", "TRAIL"),
    "TRAIL": ("TRL", "TRAIL"),
    "TRAILS": ("TRL", "TRAIL"),
    "TRL": ("TRL", "TRAIL"),
    "TRLS": ("TRL", "TRAIL"),
    "TUNEL": ("TUNL", "TUNNEL"),
    "TUNL": ("TUNL", "TUNNEL"),
    "TUNLS": ("TUNL", "TUNNEL"),
    "TUNNEL": ("TUNL", "TUNNEL"),
    "TUNNELS": ("TUNL", "TUNNEL"),
    "TUNNL": ("TUNL", "TUNNEL"),
    "TPK": ("TPKE", "TURNPIKE"),
    "TPKE": ("TPKE", "TURNPIKE"),
    "TRNPK": ("TPKE", "TURNPIKE"),
    "TRPK": ("TPKE", "TURNPIKE"),
    "TURNPIKE": ("TPKE", "TURNPIKE"),
    "TURNPK": ("TPKE", "TURNPIKE"),
    "UNDERPASS": ("UPAS", "UNDERPASS"),
    "UN": ("UN", "UNION"),
    "UNION": ("UN", "UNION"),
    "UNIONS": ("UNS", "UNIONS"),
    "VALLEY": ("VLY", "VALLEY"),
    "VALLY": ("VLY", "VALLEY"),
    "VLLY": ("VLY", "VALLEY"),
    "VLY": ("VLY", "VALLEY"),
    "VALLEYS": ("VLYS", "VALLEYS"),
    "VLYS": ("VLYS", "VALLEYS"),
    "VDCT": ("VIA", "VIADUCT"),
    "VIA": ("VIA", "VIADUCT"),
    "VIADCT": ("VIA", "VIADUCT"),
    "VIADUCT": ("VIA", "VIADUCT"),
    "VIEW": ("VW", "VIEW"),
    "VW": ("VW", "VIEW"),
    "VIEWS": ("VWS", "VIEWS"),
    "VWS": ("VWS", "VIEWS"),
    "VILL": ("VLG", "VILLAGE"),
    "VILLAG": ("VLG", "VILLAGE"),
    "VILLAGE": ("VLG", "VILLAGE"),
    "VILLG": ("VLG", "VILLAGE"),
    "VILLIAGE": ("VLG", "VILLAGE"),
    "VLG": ("VLG", "VILLAGE"),
    "VILLAGES": ("VLGS", "VILLAGES"),
    "VLGS": ("VLGS", "VILLAGES"),
    "VILLE": ("VL", "VILLE"),
    "VL": ("VL", "VILLE"),
    "VIS": ("VIS", "VISTA"),
    "VIST": ("VIS", "VISTA"),
    "VISTA": ("VIS", "VISTA"),
    "VST": ("VIS", "VISTA"),
    "VSTA": ("VIS", "VISTA"),
    "WALK": ("WALK", "WALK"),
    "WALKS": ("WALKS", "WALKS"),
    "WALL": ("WALL", "WALL"),
    "WAY": ("WAY", "WAY"),
    "WY": ("WAY", "WAY"),
    "WAYS": ("WAYS", "WAYS"),
    "WELL": ("WL", "WELL"),
    "WELLS": ("WLS", "WELLS"),
    "WLS": ("WLS", "WELLS"),
}
