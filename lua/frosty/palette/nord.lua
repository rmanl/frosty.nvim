---@type frosty.Theme
local M = {
	alt = "#6e7f86",
	alt_bg = "#25282f",
	bg = "#090e13",
	comment = "#4f5159",
	constant = "#b0b3b0",
	fg = "#c8cac8",
	func = "#8f918a",
	keyword = "#8f918a",
	line = "#090e13",
	number = "#8b9a97",
	operator = "#978e96",
	property = "#c8cac8",
	string = "#aaa083",
	type = "#8f866f",
	visual = "#25282f",
	diag_red = "#6e7f86",
	diag_blue = "#8f918a",
	diag_yellow = "#6e7f86",
	diag_green = "#8f6a64",
	mini_diff_add = "#86907e",
	mini_diff_cha = "#aaa083",
	mini_diff_del = "#a97f78",
	indent_hl = "#25282f",
}

---@type frosty.Theme.Terminal
M.colormap = {
	black = M.alt_bg,
	grey = M.comment,
	red = M.diag_red,
	orange = M.number,
	green = M.property,
	yellow = M.func,
	blue = M.constant,
	purple = M.keyword,
	magenta = M.type,
	cyan = M.string,
	white = M.fg,
}

return M
