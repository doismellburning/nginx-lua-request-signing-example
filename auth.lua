local args = ngx.req.get_uri_args()
local headers = ngx.req.get_headers()
local sig = headers["Authorization"]
if sig == nil then
	ngx.header["WWW-Authenticate"] = "Mine"
	ngx.exit(ngx.HTTP_UNAUTHORIZED)
elseif sig == "Mine secret" then
	ngx.exit(ngx.HTTP_OK)
else
	ngx.exit(ngx.HTTP_FORBIDDEN)
end
