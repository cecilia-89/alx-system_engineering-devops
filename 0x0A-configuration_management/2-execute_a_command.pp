#kills a process

exec {
	'pkill':
	command => 'pkill -9 killmenow'
}