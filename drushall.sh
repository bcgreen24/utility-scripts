for dir in ~/htdocs/drupal/drupal/sites/*
do
    #-----------------------------------
    # Derek's new code
    #-----------------------------------
    echo ' * * * Working in ' $dir
    (cd $dir && /opt/webstack/php/5.2/bin/php /local/users/drupadm/drush/drush.php "$@")

    # # Test to make sure arg expansion works as expected
    # for arg in "$@"
    # do
    #     echo ${arg}
    # done

    #-----------------------------------
    # Bryan's original code
    #-----------------------------------
    # if [ $dir = "/local/users/drupadm/htdocs/drupal/drupal/sites/all" ]
    # then
    #   continue
    # fi
    # (cd $dir && /opt/webstack/php/5.2/bin/php /local/users/drupadm/drush/drush.php $1)
done

