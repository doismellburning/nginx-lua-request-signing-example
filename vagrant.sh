apt-get update
apt-get install --yes --quiet nginx-extras
echo """
server {
	root /usr/share/nginx/www;

	location / {
		access_by_lua_file '/vagrant/auth.lua';
	}
}
""" > /etc/nginx/sites-enabled/default
service nginx restart
