from pylabel import importer

path_to_annotations = 'wd_speciesid/data/intermediate/coco.json'
outpath = 'wd_speciesid/data/intermediate/yolo.json'
importer.ImportCoco(path_to_annotations).export.ExportToYoloV5(outpath)