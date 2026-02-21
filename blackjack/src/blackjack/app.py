"""
Train your mind counting cards.

Copyright (c) 2026, Lif28
Licensed under the MIT License - see LICENSE file for details
"""

import toga
import random
import asyncio
from toga.style.pack import COLUMN, ROW, CENTER, Pack


class BlackJack(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        self.HI_LO_VALUES = {
            '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
            '7': 0, '8': 0, '9': 0,
            '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
        }
        
        SUITS = ['H', 'D', 'C', 'S'] 
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [f"{rank}{suit}" for rank in RANKS for suit in SUITS]

        self.main_window = toga.MainWindow(title=self.formal_name)

        # Home button
        home_command = toga.Command(
            self.show_home,
            text='Home',
            tooltip='Return to home screen',
            group=toga.Group.APP
        )
        self.commands.add(home_command)

        self.show_home()
        self.main_window.show()

    def show_home(self, widget=None):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, align_items=CENTER, flex=1))
        
        logo = toga.ImageView(
        image=toga.Image("resources/logo.png"), style=Pack(margin=20, width=120, height=120))

        # Resets
        self.input_box = None
        self.is_running = False
        self.current_index = 0
        self.running_count = 0
        
        # Deletes timed mode's task if running
        if hasattr(self, 'timed_task') and self.timed_task:
            self.timed_task.cancel()
            self.timed_task = None

        # Title, subtitle, butttons and info
        title = toga.Label("BlackJack Card Counter", style=Pack(margin=10, font_size=20, font_weight='bold', text_align=CENTER, color="#000000"))
        subtitle = toga.Label("Train using the Hi-Lo method", style=Pack(margin=(5, 20, 30, 20), font_size=12, text_align=CENTER, color="#3f3f3f"))

        normal_button = toga.Button("Normal Mode", on_press=self.normal_mode, style=Pack(margin=15, width=200, height=65))
        timed_button = toga.Button("Timed Mode", on_press=self.timed_mode, style=Pack(margin=15, width=200, height=65))
        bottom_spacer = toga.Box(style=Pack(flex=0.5))
        middle_spacer = toga.Box(style=Pack(flex=1))
        top_spacer = toga.Box(style=Pack(flex=0.5))
        version = toga.Label("v1.0.0", style=Pack(margin=10, font_size=11, text_align=CENTER, color='#888888'))
        divider = toga.Divider(style=Pack(margin=(5, 40)))

        # Adds everything to home
        self.main_box.add(top_spacer)
        self.main_box.add(logo)
        self.main_box.add(title)
        self.main_box.add(subtitle)
        self.main_box.add(middle_spacer)
        self.main_box.add(normal_button)
        self.main_box.add(timed_button)
        self.main_box.add(bottom_spacer)
        self.main_box.add(divider)
        self.main_box.add(version)

        self.main_window.content = self.main_box

    def normal_mode(self, widget):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, align_items=CENTER, background_color='#ffffff'))
        # shuffle deck
        random.shuffle(self.deck)
        self.choices = random.choices(range(5,53,5), k=3)

        # Check
        if hasattr(self, 'input_box') and self.input_box: 
            self.main_box.remove(self.input_box)

        # First card
        first_card = self.deck[self.current_index]
        self.card_image = toga.Image(f"cards/{first_card}.jpg")
        self.image_view = toga.ImageView(image=self.card_image, style=Pack(flex=1))

        # Random feedback
        self.feedback_label = toga.Label("", style=Pack(direction=COLUMN, margin=20, text_align=CENTER))
        self.feedback_label.text = ""

        #Button
        self.next_button = toga.Button("Next", on_press=self.next, style=Pack(flex=0, margin=5, width=200))

        # Adds everything to main_box
        self.main_box.clear()
        self.main_box.add(self.image_view)
        self.main_box.add(self.next_button)
        self.main_box.add(self.feedback_label)

        self.main_window.content = self.main_box

    def next(self, widget):
        # Checks for input
        if hasattr(self, 'input_box') and self.input_box:
            if not self.input.value:
                self.feedback_label.text = "⚠️ Insert the running count."
                return
            
            if int(self.input.value) == self.running_count:
                self.feedback_label.text = "✓ Correct!"
            else:
                self.feedback_label.text = f"✗ Wrong! It was: {self.running_count}"

            self.main_box.remove(self.input_box)
            self.input_box = None
        else:
            self.feedback_label.text = ""           

            # Adds card to the running count
            current_card = self.deck[self.current_index]
            rank = current_card[:-1]
            self.running_count += self.HI_LO_VALUES[rank]
        
        self.current_index += 1

        # Re-shuffles the deck
        if self.current_index > 51:
            random.shuffle(self.deck)
            self.current_index, self.running_count = 0,0

        # Asks running count
        if self.current_index in self.choices:
            # Hides the card
            self.main_box.remove(self.image_view)

            # Removes the button to add it later
            self.main_box.remove(self.next_button)

            title = toga.Label(
                "What's the running count?",
                style=Pack(
                    margin=10,
                    font_size=16,
                    font_weight='bold',
                    text_align=CENTER
                )
            )

            self.input = toga.TextInput(style=Pack(width=150, margin=10, font_size=16))
            self.input_box = toga.Box(style=Pack(direction=COLUMN, margin=10, align_items=CENTER))

            self.input_box.add(title)
            self.input_box.add(self.input)
            self.main_box.add(self.input_box)
            self.main_box.add(self.next_button) 
            # Doesn't show the next card because you have to insert the running count first
            return 
        
        if self.image_view not in self.main_box.children:
            self.main_box.insert(0, self.image_view)

        # New card
        next_card = self.deck[self.current_index]
        self.card_image = toga.Image(f"cards/{next_card}.jpg")
        self.image_view.image = self.card_image
    
    def timed_mode(self, widget):
        print(self.running_count)
        self.main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, align_items=CENTER, background_color='#ffffff'))

        # Important variables for start_timed_mode
        self.speed = 1
        self.is_running = True

        # shuffle deck
        random.shuffle(self.deck)
        self.choices = random.choices(range(5,53,5), k=3)

        # First card
        first_card = self.deck[self.current_index]
        self.card_image = toga.Image(f"cards/{first_card}.jpg")
        self.image_view = toga.ImageView(image=self.card_image, style=Pack(flex=1))

        # Random feedback
        self.feedback_label = toga.Label("", style=Pack(direction=COLUMN, margin=20, text_align=CENTER))
        
        # Button & slider
        self.stop_button = toga.Button(
            "Stop",
            on_press=self.stop_timed,
            style=Pack(margin=5, width=100)
        )
        self.speed_slider = toga.Slider(min=0.5, max=2, tick_count=7, value=self.speed, style=Pack(width=200))
        
        # Adds everything to main_box
        self.main_box.clear()
        self.main_box.add(self.image_view)
        self.main_box.add(self.feedback_label)
        self.main_box.add(self.speed_slider)
        self.main_box.add(self.stop_button)
        
        if hasattr(self, 'timed_task') and self.timed_task:
            self.timed_task.cancel()

        
        self.timed_task = asyncio.create_task(self.start_timed_mode())    
        self.main_window.content = self.main_box


    async def start_timed_mode(self, widget=None):
        while True:
            if not self.is_running:
                await asyncio.sleep(0.1)  
                continue

            if hasattr(self, 'show_feedback_delay') and self.show_feedback_delay:
                await asyncio.sleep(1.5) # feedback for 1.5 sec
                self.show_feedback_delay = False
                # Re-adds the card
                if self.image_view not in self.main_box.children:
                    self.main_box.insert(0, self.image_view)
            
            # Waits 
            await asyncio.sleep(self.speed_slider.value)

            # Counts the card 
            current_card = self.deck[self.current_index]
            rank = current_card[:-1]
            self.running_count += self.HI_LO_VALUES[rank]
            
            self.feedback_label.text = ""  

            # Asks running count
            if self.current_index in self.choices:
                self.current_index += 1

                if self.current_index > 51:
                    random.shuffle(self.deck)
                    self.current_index, self.running_count = 0, 0

                self.main_box.remove(self.image_view)
                self.main_box.remove(self.speed_slider)
                self.main_box.remove(self.stop_button)

                title = toga.Label(
                    "What's the running count?",
                    style=Pack(margin=20, font_size=18, font_weight='bold', text_align=CENTER)
                )
                
                self.input = toga.TextInput(style=Pack(width=150, margin=10, font_size=16))
                self.input_box = toga.Box(style=Pack(direction=COLUMN, margin=10, align_items=CENTER))
                
                # Checks the running count
                submit_button = toga.Button(
                    "Submit",
                    on_press=self.check_count_timed_mode,
                    style=Pack(margin=5, width=150)
                )
                
                # main box
                self.input_box.add(title)
                self.input_box.add(self.input)
                self.input_box.add(submit_button)
                self.main_box.add(self.input_box)
                
                # Adds the new card
                next_card = self.deck[self.current_index]
                self.card_image = toga.Image(f"cards/{next_card}.jpg")
                self.image_view.image = self.card_image

                self.is_running = False
                continue 

            self.current_index += 1
            
            if self.current_index > 51:
                random.shuffle(self.deck)
                self.current_index, self.running_count = 0, 0

            # New card
            next_card = self.deck[self.current_index]
            self.card_image = toga.Image(f"cards/{next_card}.jpg")
            self.image_view.image = self.card_image 

            # Remembers the speed also after the question about the running count
            self.speed = self.speed_slider.value
            self.feedback_label.text = ""  
    
    def check_count_timed_mode(self, widget):
        if not self.input.value:
            self.feedback_label.text = "⚠️ Insert the running count."
            return
    
        if int(self.input.value) == self.running_count:
            self.feedback_label.text = "✓ Correct!"
        else:
            self.feedback_label.text = f"✗ Wrong! It was: {self.running_count}"
        
        # Removes input
        self.main_box.remove(self.input_box)
        self.input_box = None

        if self.image_view not in self.main_box.children:
            self.main_box.insert(0, self.image_view)
        
        self.speed_slider = toga.Slider(min=0.5, max=2, tick_count=7, value=self.speed, style=Pack(width=200))
        self.stop_button = toga.Button("Stop", on_press=self.stop_timed, style=Pack(margin=5, width=100))
        self.main_box.add(self.speed_slider)
        self.main_box.add(self.stop_button)

        # Back to timed mode 
        self.show_feedback_delay = True
        self.is_running = True

    def stop_timed(self, widget):
        # Stops the timed mode
        self.is_running = False  
        self.stop_button.text = "Resume"
        self.stop_button.on_press = self.resume_timed

    def resume_timed(self, widget):
        self.is_running = True
        self.stop_button.text = "Stop"
        self.stop_button.on_press = self.stop_timed

def main():
    return BlackJack()
