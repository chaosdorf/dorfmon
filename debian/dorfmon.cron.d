# /etc/cron.d/dorfmap-helpers

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

  *    *   *   *   *   www-data  update-roomstatus
  *    *   *   *   *   www-data  publish-prometheus
  */4  *   *   *   *   www-data  nice gather-hosts
  */4  *   *   *   *   www-data  nice gather-temperatures
  59   *   *   *   *   www-data  nice gather-doorcount
