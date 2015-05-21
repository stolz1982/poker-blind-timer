#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk, time, sys
from threading import Timer

class Base:

        def on_quit_click(self, widget):
                print "Beendet"
                gtk.mainquit()
		sys.exit(0)

        def on_button_click(self, widget):
                # Blinderhoehung
                radio = [r for r in self.button.get_group() if r.get_active()][0]
                radiolabel = radio.get_label()

                if radiolabel == "Double":
                        be = 2
                elif radiolabel == "Triple":
                        be = 3
                # Blindpruefung
                small_blind = int(self.entry1.get_text())
                big_blind = int(self.entry2.get_text())

                if small_blind == "":
                        self.label7.set_markup("<span foreground='red'>Fehler: Kein Start moeglich, es fehlt der SMALL Blind!!!</span>")
                        return False

                if big_blind == "":
                        self.label7.set_markup("<span foreground='red'>Fehler: Kein Start moeglich, es fehlt der BIG Blind!!!</span>")
                        return False

                if small_blind >= big_blind:
                        print "Small groesser / gleich Blind " + str(small_blind) + " | " + str(big_blind)
                        self.label7.set_markup("<span foreground='red'>Fehler: Kein Start moeglich, der SMALL Blind ist groesser/gleich als der Big Blind!!!</span>")
                        return False

                # Intervalpruefung
                interval = self.entry3.get_text()
                if interval == "":
                        print "Interval leer"
                        self.label7.set_markup("<span foreground='red'>Fehler: Kein Start moeglich, der Interval ist leer!!!</span>")
                        return False



                # Wenn alles okay ist dann wird die naechsten Blinderhoehung eingeblendet
                # self.label7.set_markup("<span foreground='black'>Blinderhoehung: Small blind</span>")
                var = "Naechste Runde Blinderhoehung Small Blind: " + str(int(small_blind) * int(be)) + " | Big Blind: " + str(int(big_blind) * int(be))
                self.label7.set_markup("<span foreground='blue'>{0}</span>".format(var))

                i = int(self.entry3.get_text()) * 60
                while i > 0:
                        i-=1
                        time.sleep(1)
			# self.progressbar1.set_fraction(fraction) 
                        self.entry4.set_text(str(i))
                        if i == 300:
                                self.label7.set_markup("<span foreground='black'>{0}</span>".format(var))
			if i < 120:
				self.label7.set_markup("<span foreground='red'>{0}</span>".format(var)) 
			if i < 11:	
				print("\a")	
			
			if i == 1:
				small_blind = int(small_blind) * int(be)
				big_blind = int(big_blind) * int(be)
	        	        self.entry1.set_text(str(int(small_blind)))
        	       		self.entry2.set_text(str(int(big_blind)))
		                var = "Naechste Runde Blinderhoehung Small Blind: " + str(int(small_blind) * int(be)) + " | Big Blind: " + str(int(big_blind) * int(be))
		                self.label7.set_markup("<span foreground='blue'>{0}</span>".format(var))
				i = int(self.entry3.get_text()) * 60

                        while gtk.events_pending():
                               gtk.main_iteration_do(False)

			
	def callback(self, widget, data=None):
	        print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])

	def __init__(self):
		
		self.window = gtk.Window()
		self.window.connect('destroy', lambda w: gtk.main_quit())
		# self.window.set_size_request(900, 600)
		self.window.set_title("Poker Counter")
		
		self.boxV = gtk.VBox()
		self.window.add(self.boxV)

		self.box = gtk.HBox()
		self.boxV.pack_start(self.box)

		self.label1 = gtk.Label("Small Blind:")
		self.box.pack_start(self.label1)

		self.entry1 = gtk.Entry()
		self.box.pack_start(self.entry1)
		self.entry1.set_text("50")

		self.hs2 = gtk.VSeparator()
		self.box.pack_start(self.hs2)

		self.label2 = gtk.Label("Big Blind:")		
		self.box.pack_start(self.label2)
		
		self.entry2 = gtk.Entry()
		self.box.pack_start(self.entry2)
		self.entry2.set_text("100")

                self.box2 = gtk.VBox()
		
		self.button = gtk.RadioButton(None, "Double")
		self.button.connect("toggled", self.callback, "2")
		
		self.box2.pack_start(self.button, True, True, 0)
		self.button.show()

                self.button = gtk.RadioButton(self.button, "Triple")
                self.button.connect("toggled", self.callback, "3")
                self.box2.pack_start(self.button, True, True, 0)
                self.button.show()

                self.hs3 = gtk.VSeparator()
                self.box.pack_start(self.hs3)


                self.label3 = gtk.Label("Blinderhoehung:")
		self.box.pack_start(self.label3)
				
		self.box.pack_start(self.box2)	

		self.hs1 = gtk.HSeparator()
		self.boxV.pack_start(self.hs1)
	
		self.boxH2 = gtk.HBox()
		self.boxV.pack_start(self.boxH2)

		self.label4 = gtk.Label("Interval:")
		self.boxH2.pack_start(self.label4)
		
		self.entry3 = gtk.Entry()
		self.entry3.set_tooltip_text("Das Interval entspricht der Rundenlaenge!")
		self.boxH2.pack_start(self.entry3)
		self.entry3.set_text("15")
		
		self.label5 = gtk.Label("Minuten")
		self.boxH2.pack_start(self.label5)

		self.vs1 = gtk.VSeparator()
		self.boxH2.pack_start(self.vs1)
		
		self.label6 = gtk.Label("Verbleibende Zeit:")
		self.boxH2.pack_start(self.label6)
		
		self.entry4 = gtk.Entry()
		self.boxH2.pack_start(self.entry4)

		self.label7 = gtk.Label("Sekunden")
		self.boxH2.pack_start(self.label7)		

                self.hs3 = gtk.HSeparator()
                self.boxV.pack_start(self.hs3)

		self.label7 = gtk.Label(" ")
		self.boxV.pack_start(self.label7)

		self.hs2 = gtk.HSeparator()
		self.boxV.pack_start(self.hs2)
		
		self.progressbar1 = gtk.ProgressBar(adjustment=None)
		self.boxV.pack_start(self.progressbar1)

		self.button_start = gtk.Button("Start")
		self.button_start.connect( 'clicked', self.on_button_click )
		self.button_start.set_tooltip_text("Los geht die Wahnsinnsrunde")
		self.boxV.pack_start(self.button_start)

                self.button_quit = gtk.Button("Quit")
                self.button_quit.connect( 'clicked', self.on_quit_click )
                self.boxV.pack_start(self.button_quit)

	
		self.window.show_all()

	def main(self):
		gtk.main()

if __name__ == "__main__":
  base = Base()
  base.main()
