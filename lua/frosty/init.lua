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

---Toggle between light/dark variants.
function M.toggle_variant()
	if vim.o.background == "light" then
		vim.o.background = "dark"
		vim.api.nvim_command("colorscheme " .. M.__opts.theme)
	else
		vim.api.nvim_command("colorscheme frosty-day")
	end
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
	if vim.o.background == "light" then
		M.__opts.variant = "light"
	else
		M.__opts.variant = "dark"
	end
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
	if M.__opts.toggle_variant_key then
		vim.keymap.set(
			"n",
			M.__opts.toggle_variant_key,
			'<cmd>lua require("frosty").toggle_variant()<cr>',
			{ noremap = true, silent = true }
		)
	end
	M.__setup_called = true
end

return M
