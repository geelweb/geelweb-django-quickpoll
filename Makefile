
git:
	@echo "installing git pre-commit hook..."
	@git clone git://github.com/geelweb/git-utils.git /tmp/git-utils
	@cp /tmp/git-utils/pre-commit .git/hooks/
	@rm -rf /tmp/git-utils
