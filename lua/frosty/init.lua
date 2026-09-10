local Config = require("frosty.config")
local M = {
	---@type frosty.Config
	__opts = {},
	__setup_called = false,
}

---Returns a read-only copy of the config.
---@return frosty.Config
function M.options()
	return vim.deepcopy(M.__opts)
end

---Apply the colorscheme (same as `:colorscheme frosty`).
---@param theme string?
function M.load(theme)
	M.__opts.theme = theme or M.__opts.theme
	vim.cmd("hi clear")
	if vim.fn.exists("syntax_on") then
		vim.cmd("syntax reset")
	end
	vim.o.termguicolors = true
	vim.g.colors_name = M.__opts.theme
	require("frosty.highlights").setup()
	require("frosty.terminal").setup()
end

---Set the config options.
---@param opts frosty.Config
function M.setup(opts)
	if M.__setup_called then
		return
	end

	---@type frosty.Config
	M.__opts = vim.tbl_deep_extend("force", Config.default, opts or {})
	M.__theme = M.__opts.theme
	M.__setup_called = true
end

return M
