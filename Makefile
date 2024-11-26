# Default target
.PHONY: run create_day

# Dynamic run target
run:
	@read -p "Enter the day number (e.g., 01, 02): " daynum; \
	python 2024/day_$${daynum}/day_$${daynum}.py

# Run specific day directly
run_day:
	python 2024/day_$(DAY)/day_$(DAY).py

# Create a new day's folder and files
create_day:
	@read -p "Enter the day number (e.g., 01, 02): " daynum; \
	day_folder="2024/day_$${daynum}"; \
	mkdir -p $${day_folder}; \
	cp 2024/day_template.py $${day_folder}/day_$${daynum}.py; \
	touch $${day_folder}/day_$${daynum}_input.txt; \
	touch $${day_folder}/day_$${daynum}_test_input.txt; \
	echo "Created files for Day $${daynum} in $${day_folder}"