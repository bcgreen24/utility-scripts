for dir in ~/htdocs/drupal/drupal/sites/*
  do
    if [ $dir = "/local/users/drupadm/htdocs/drupal/drupal/sites/all" ]
    then
      continue
    fi
    echo $dir
    (cd $dir && /opt/webstack/php/5.2/bin/php /local/users/drupadm/drush/drush.php $1)
  done
