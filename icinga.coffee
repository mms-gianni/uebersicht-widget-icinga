config =
  title: 'Monitoring'
  username: 'CHANGEME'
  password: 'CHANGEME'
  url: 'monitor.yourdomain.com'
  topposition: '420px'
  leftposition: '10px'

command: "./icinga.widget/icinga.py #{ config.username }:#{ config.password } #{ config.url } #{ config.title }" 

refreshFrequency: 50000

style: """
	top: #{config.topposition}
	left: #{config.leftposition}

	color: #fff
	font-family: Helvetica Neue
	background: rgba(#fff, .3)
	padding 10px 15px 15px
	border-radius: 5px
	font-size: 11px

	#widget
		clear: both
		position: relative
		
	.green
		color: #66FF00
	.yellow
		color: #FFDF00
	.red
		color: #FF2400

	#cell
		/*float: left*/
		padding: 2px
	
	#header
		width: 100%
		text-transform: uppercase
		font-size: 14px
		font-weight: bold
		padding-bottom: 8px
"""
