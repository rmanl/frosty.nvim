local M = {}

function M.get()
	---@type frosty.Config
	local Config = require("frosty").options()
	local colors = require("frosty.terminal").colors(true)
	local plain = Config.plugin.lualine.plane
	local bold = Config.plugin.lualine.bold
	local c = {
		norm = colors.blue,
		ins = colors.yellow,
		vis = colors.purple,
		rep = colors.cyan,
		comm = colors.orange,
		fg_dim = colors.comment,
		vcs = colors.alt,
		bg_b = colors.visual,
		bg_c = colors.line,
		dark = colors.bg,
		none = "none",
	}

	local hl = {}

	hl.normal = {
		a = {
			bg = plain and c.none or c.norm,
			fg = plain and c.norm or c.dark,
			gui = bold and "bold" or c.none,
		},
		b = { bg = plain and c.none or c.bg_b, fg = c.vcs },
		c = { bg = plain and c.none or c.bg_c, fg = c.fg_dim },
	}

	hl.insert = {
		a = {
			bg = plain and c.none or c.ins,
			fg = plain and c.ins or c.dark,
			gui = bold and "bold" or c.none,
		},
	}

	hl.visual = {
		a = {
			bg = plain and c.none or c.vis,
			fg = plain and c.vis or c.dark,
			gui = bold and "bold" or c.none,
		},
	}

	hl.replace = {
		a = {
			bg = plain and c.none or c.rep,
			fg = plain and c.rep or c.dark,
			gui = bold and "bold" or c.none,
		},
	}

	hl.command = {
		a = {
			bg = plain and c.none or c.comm,
			fg = plain and c.comm or c.dark,
			gui = bold and "bold" or c.none,
		},
	}

	return hl
end

return M
