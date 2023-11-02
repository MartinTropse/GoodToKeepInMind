import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\Users\MartinAndersson\Calluna AB\MAL0001 Åtgärdsplan Sörfjärden - General\Arbetsdokument\Script\ArcpyBeräkning\MAL0001_SörfjärdenUnderlag.gdb"

# Specify the path to the feature class
feature_class = "Diken_Vallar_LstD_Sör_Buffer"
categorical_raster = "NMD_2018_Sorfjarden_Clip"


Fields = arcpy.ListFields(feature_class)
FieldNames = [field.name for field in Fields]

raster_desc = arcpy.Describe(categorical_raster)
raster_spatial_ref = raster_desc.spatialReference

buffer_desc = arcpy.Describe(feature_class)
buffer_spatial_ref = buffer_desc.spatialReference
buffer_spatial_ref.name == raster_spatial_ref.name # Check if the layer has the same coorindate system. 

# Create a feature layer from the feature class, which is necessary to run feature by feature operations. 
feature_layer = arcpy.MakeFeatureLayer_management(feature_class, "FeatureLayer")

# Iterate through each feature
with arcpy.da.SearchCursor(feature_layer, ["SHAPE@", "OBJECTID_1"]) as cursor:
    for row in cursor:
        shape = row[0]
        object_id = row[1]
        print(type(shape)) # Should return something like this in order to work: <class 'arcpy.arcobjects.geometries.Polygon'>
        # Create a new feature class based on the geometry
        out_feature_class = f"Feature_{object_id}"
        mask = arcpy.sa.ExtractByMask(categorical_raster, shape)
        out_table = f"Buffer_{object_id}_SummaryTable.csv"        
        arcpy.ia.SummarizeCategoricalRaster(mask, out_table)