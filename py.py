    def on_pie_click(self, event):
        """
        Handles click events on the pie chart segments.
        """
        item = self.chart_canvas.find_closest(event.x, event.y)  # Find the item closest to the click
        tags = self.chart_canvas.gettags(item)  # Get the tags of the item
        if tags:
            label = tags[0]  # Get the first tag (the label)
            for meal, calories in zip(self.meal_labels, self.meal_calories):
                if meal == label:
                    messagebox.showinfo("Meal Info", f"{meal}: {calories} CALORIES")  # Show meal info in a message box

    def create_meal_inputs(self, frame):
        """
        Creates input fields and bars for each meal.
        """
        self.meal_entries = []
        self.meal_bars = []
        meals = [("BREAKFAST", self.meal_calories[0]), ("LUNCH", self.meal_calories[1]), ("DINNER", self.meal_calories[2])]
        for i, meal in enumerate(meals):
            # Create a frame for each meal input
            meal_frame = tk.Frame(frame)
            meal_frame.pack(fill="x", pady=5, padx=10)
            # Label for the meal
            label = tk.Label(meal_frame, text=meal[0], font=("Helvetica", 12))
            label.pack(side="left")
            # Entry field for the meal calories
            entry = tk.Entry(meal_frame, width=10)
            entry.insert(0, meal[1])
            entry.pack(side="left")
            self.meal_entries.append(entry)

            # Create bar for meal calorie limit indicator
            bar = Canvas(meal_frame, height=10, bg='white')
            bar.pack(fill="x", padx=10, pady=5)
            self.meal_bars.append(bar)
            self.update_meal_bar(i, meal[1], self.calorie_limits[i])

        # Update button to apply new calorie values
        update_button = tk.Button(frame, text="Update", font=("Helvetica", 12), command=self.update_calories)
        update_button.pack(pady=10)

    def update_meal_bar(self, index, value, limit):
        """
        Updates the bar for a meal to show if the calories are within the limit.
        """
        bar = self.meal_bars[index]
        bar.delete("all")  # Clear the bar
        value = int(value)
        if value <= limit:
            bar.create_rectangle(0, 0, (value / limit) * bar.winfo_width(), 10, fill="green")  # Green bar if within limit
        else:
            bar.create_rectangle(0, 0, bar.winfo_width(), 10, fill="red")  # Red bar if over the limit

    def update_calories(self):
        """
        Updates the calorie data, redraws the pie chart, updates the progress bar and meal bars.
        """
        try:
            # Get new calorie values from the input fields
            self.meal_calories = [int(entry.get()) for entry in self.meal_entries]

            # Redraw the pie chart with new values
            self.arcs = self.draw_pie_chart(self.chart_canvas, self.meal_calories, self.colors, self.meal_labels)
            total_calories = sum(self.meal_calories)

            # Update the progress bar
            self.progress_bar.delete("all")  # Clear the progress bar
            if total_calories <= 2000:
                self.progress_bar.create_rectangle(0, 0, (total_calories / 2000) * self.progress_bar.winfo_width(), 20, fill="green")  # Green if within limit
            else:
                self.progress_bar.create_rectangle(0, 0, self.progress_bar.winfo_width(), 20, fill="red")  # Red if over the limit
            self.progress_bar.create_text(150, 10, text=f"{total_calories}/2000", anchor="e", font=("Helvetica", 10))

            # Update the meal bars
            for i, value in enumerate(self.meal_calories):
                self.update_meal_bar(i, value, self.calorie_limits[i])
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for calories.")

    def draw_pie_chart(self, canvas, data, colors, labels):
        """
        Draws a pie chart on the given canvas.
        """
        canvas.delete("all")  # Clear the canvas
        total = sum(data)  # Calculate total calories
        start_angle = 0  # Starting angle for the first segment
        arcs = []
        for i, value in enumerate(data):
            extent = (value / total) * 360  # Calculate the extent of the segment
            arc = canvas.create_arc((50, 50, 350, 350), start=start_angle, extent=extent, fill=colors[i], tags=labels[i])
            arcs.append(arc)
            start_angle += extent  # Update starting angle for the next segment
        return arcs

    def on_pie_click(self, event):
        """
        Handles click events on the pie chart segments.
        """
        item = self.chart_canvas.find_closest(event.x, event.y)  # Find the item closest to the click
        tags = self.chart_canvas.gettags(item)  # Get the tags of the item
        if tags:
            label = tags[0]  # Get the first tag (the label)
            for meal, calories in zip(self.meal_labels, self.meal_calories):
                if meal == label:
                    messagebox.showinfo("Meal Info", f"{meal}: {calories} CALORIES")  # Show meal info in a message box

    def create_meal_inputs(self, frame):
        """
        Creates input fields and bars for each meal.
        """
        self.meal_entries = []
        self.meal_bars = []
        meals = [("BREAKFAST", self.meal_calories[0]), ("LUNCH", self.meal_calories[1]), ("DINNER", self.meal_calories[2])]
        for i, meal in enumerate(meals):
            # Create a frame for each meal input
            meal_frame = tk.Frame(frame)
            meal_frame.pack(fill="x", pady=5, padx=10)
            # Label for the meal
            label = tk.Label(meal_frame, text=meal[0], font=("Helvetica", 12))
            label.pack(side="left")
            # Entry field for the meal calories
            entry = tk.Entry(meal_frame, width=10)
            entry.insert(0, meal[1])
            entry.pack(side="left")
            self.meal_entries.append(entry)

            # Create bar for meal calorie limit indicator
            bar = Canvas(meal_frame, height=10, bg='white')
            bar.pack(fill="x", padx=10, pady=5)
            self.meal_bars.append(bar)
            self.update_meal_bar(i, meal[1], self.calorie_limits[i])

        # Update button to apply new calorie values
        update_button = tk.Button(frame, text="Update", font=("Helvetica", 12), command=self.update_calories)
        update_button.pack(pady=10)

    def update_meal_bar(self, index, value, limit):
        """
        Updates the bar for a meal to show if the calories are within the limit.
        """
        bar = self.meal_bars[index]
        bar.delete("all")  # Clear the bar
        value = int(value)
        if value <= limit:
            bar.create_rectangle(0, 0, (value / limit) * bar.winfo_width(), 10, fill="green")  # Green bar if within limit
        else:
            bar.create_rectangle(0, 0, bar.winfo_width(), 10, fill="red")  # Red bar if over the limit

# Create the main application window
window = tk.Tk()
app = App(window)
window.mainloop()
