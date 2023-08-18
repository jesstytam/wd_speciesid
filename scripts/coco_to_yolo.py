from pylabel import importer

path_to_annotations = 'wd_speciesid/data/intermediate/md_coco.json'
outpath = 'wd_speciesid/data/intermediate/coco_yolo.json'
importer.ImportCoco(path_to_annotations).export.ExportToYoloV5(outpath)