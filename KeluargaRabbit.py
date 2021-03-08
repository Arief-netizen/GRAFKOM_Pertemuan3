import pygame


class KeluargaRabbit:
    def __init__(self):
        self.window = (600, 600)
        self.caption = "Tugas Pertemuan 3_Imam Arief Al Baihaqy_006_D4 MI2019A"
        self.display = pygame.display.set_mode(self.window)
        self.running = True

    def run(self):
        # Intiliazie PyGame
        pygame.init()
        display = self.display
        pygame.display.set_caption(self.caption)

        # Run PyGame
        while self.running:
            display.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            # Create KeluargaRabbit
            self.draw_KeluargaRabbit()

            # Update KeluargaRabbit
            pygame.display.update()

    def draw_KeluargaRabbit(self):

        ## Bapak Rabbit (abil) ##
        # Badan
        pygame.draw.ellipse(
            self.display,
            (255, 150, 10, 100),
            pygame.Rect(210, 275, 190, 250),
        )
        pygame.draw.ellipse(
            self.display, (255, 130, 10, 100), pygame.Rect(210, 275, 190, 250), 4
        )

        # Kepala
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(240, 160, 130, 170),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(240, 160, 130, 170), 3
        )

        # Mata Kiri
        pygame.draw.ellipse(
            self.display,
            (3, 25, 183, 255),
            pygame.Rect(282, 220, 20, 20),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(282, 220, 20, 20), 2
        )

        # Mata Kanan
        pygame.draw.ellipse(
            self.display,
            (3, 25, 183, 255),
            pygame.Rect(310, 220, 20, 20),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(310, 220, 20, 20), 2
        )

        # Mulut
        pygame.draw.ellipse(
            self.display,
            (255, 0, 0, 255),
            pygame.Rect(285, 280, 45, 37),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(285, 280, 45, 37), 2
        )

        # Tambahan Mulut
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(266, 293, 80, 25),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(285, 293, 44, 2), 2
        )
        
        # Gigi
        pygame.draw.rect(
            self.display, (255, 255, 255, 255), pygame.Rect(300, 288, 15, 17)
        )
        pygame.draw.ellipse(
            self.display, (100, 20, 20, 100), pygame.Rect(306, 294, 3, 14), 2
        )

        # Telinga Kiri
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 100, 20),
        )
        surface = pygame.transform.rotate(surface, -55)
        self.display.blit(surface, (149, 78))

        # Telinga Kanan
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 100, 20),
        )
        surface = pygame.transform.rotate(surface, 55)
        self.display.blit(surface, (322, 78))


        
        ## Abang Rabbit (arief) ##
        # Badan
        pygame.draw.ellipse(
            self.display,
            (255, 150, 10, 100),
            pygame.Rect(80, 405, 90, 120),
        )
        pygame.draw.ellipse(
            self.display, (255, 130, 10, 100), pygame.Rect(80, 405, 90, 120), 4
        )

        # Kepala
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(96.5, 358, 60, 77),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(96.5, 358, 60, 77), 3
        )

        # Mata Kiri
        pygame.draw.ellipse(
            self.display,
            (3, 120, 183, 255),
            pygame.Rect(114, 380, 11, 11),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(114, 380, 11, 11), 2
        )

        # Mata Kanan
        pygame.draw.ellipse(
            self.display,
            (3, 120, 183, 255),
            pygame.Rect(128, 380, 11, 11),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(128, 380, 11, 11), 2
        )

        # Mulut
        pygame.draw.ellipse(
            self.display,
            (255, 0, 0, 255),
            pygame.Rect(116, 404, 22, 17),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(116, 404, 22, 17), 2
        )

        # Tambahan Mulut
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(110, 412, 32, 15),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(116, 412, 21, 2), 2
        )
        
        # Gigi
        pygame.draw.rect(
            self.display, 
            (255, 255, 255, 255), 
            pygame.Rect(123, 409, 8, 10)
        )
        pygame.draw.ellipse(
            self.display, (100, 20, 20, 100), pygame.Rect(126, 413, 2, 9), 2
        )

        # Telinga Kiri
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 60, 10),
        )
        surface = pygame.transform.rotate(surface, -55)
        self.display.blit(surface, (3, 306))

        # Telinga Kanan
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 60, 10),
        )
        surface = pygame.transform.rotate(surface, 55)
        self.display.blit(surface, (133, 275))


        ## Adik Rabbit (al baihaqy) ##
        # Badan
        pygame.draw.ellipse(
            self.display,
            (255, 150, 10, 100),
            pygame.Rect(440, 437, 60, 87),
        )
        pygame.draw.ellipse(
            self.display, (255, 130, 10, 100), pygame.Rect(440, 437, 60, 87), 4
        )

        # Kepala
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(450, 405, 42, 53),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(450, 405, 42, 53), 3
        )

        # Mata Kiri
        pygame.draw.ellipse(
            self.display,
            (0, 0, 0, 255),
            pygame.Rect(464, 421, 7, 7),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(464, 421, 7, 7), 2
        )

        # Mata Kanan
        pygame.draw.ellipse(
            self.display,
            (0, 0, 0, 255),
            pygame.Rect(472, 421, 7, 7),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(472, 421, 7, 7), 2
        )

        # Mulut
        pygame.draw.ellipse(
            self.display,
            (255, 0, 0, 255),
            pygame.Rect(464, 437, 16, 10),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(464, 437, 16, 10), 2
        )

        # Tambahan Mulut
        pygame.draw.ellipse(
            self.display,
            (100, 20, 20, 100),
            pygame.Rect(462, 442, 20, 10),
        )
        pygame.draw.ellipse(
            self.display, (150, 150, 150, 150), pygame.Rect(465, 442, 13, 2), 2
        )
        
        # Gigi
        pygame.draw.rect(
            self.display, 
            (255, 255, 255, 255), 
            pygame.Rect(470, 441, 5, 6)
        )
        pygame.draw.ellipse(
            self.display, (100, 20, 20, 100), pygame.Rect(472, 444, 1, 8), 2
        )

        # Telinga Kiri
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 35, 6),
        )
        surface = pygame.transform.rotate(surface, -55)
        self.display.blit(surface, (365, 375))

        # Telinga Kanan
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (255, 145, 10, 255),
            pygame.Rect(0, 0, 35, 6),
        )
        surface = pygame.transform.rotate(surface, 55)
        self.display.blit(surface, (476, 322))