-- string functions
string.split = function(str, delimiter)
	local res = {}
	local from = 1

	local delimFrom, delimTo = string.find(str, delimiter, from)

	while delimFrom do
		table.insert(result, string.sub(str, from, delimFrom - 1))
		from = delimTo + 1
		delimFrom, delimTo = string.find(str, delimiter, from)
	end

	table.insert(result, string.sub(str, from))

	return res
end
