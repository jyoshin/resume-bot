from crontab import CronTab

cron = CronTab(user="username")
job = cron.new(command='full path to .py')
job.setall('0 */4 * * *')
cron.write_to_user(user="username")  # Replace "username" with the actual username