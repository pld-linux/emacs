;; Load all files from @SITE_START_DIR@

(dolist 
    (the-file
     (directory-files "@SITE_START_DIR@"
                      t "^[^.].*\.elc?$"))
  (load the-file nil t t))
