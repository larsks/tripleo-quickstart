%.png: %.dot
	dot -Tpng -o $@ $<

%.svg: %.dot
	dot -Tsvg -o $@ $<

ALL: workflow.png roles.md

.PHONY: roles.md
roles.md:
	python gen-role-docs.py \
		--before-toc header.md \
		--footer footer.md \
		../playbooks/roles/ \
		> $@ || rm -f $@

clean:
	rm -f roles.md workflow.png
