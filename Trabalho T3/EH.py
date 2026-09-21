# Nomes dos integrantes do grupo:
# Danielly Priscila Silva de Castro - RA: F35FBB4 - CC5P17
# Dayane Karoline Silva de Castro - RA: F35BBA0 - CC6P17
# Sérgio Antônio Vieira Corrêa da Silva - RA: R079597 - CC6P17

import cv2

def equalizar_imagem(caminho_imagem):
    # Carregar a imagem colorida (o OpenCV já carrega em BGR)
    img_bgr = cv2.imread(caminho_imagem)
    
    # Converter para YUV para a equalização
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

    # Aplicar a equalização de histograma no canal de luminância (Y, índice 0)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

    # Converter a imagem equalizada de volta para o espaço de cores padrão do OpenCV (BGR)
    img_equalizada_bgr = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    # Opção para juntar as duas imagens lado a lado na mesma janela
    # Se preferir janelas separadas, remova esta linha e use imshow para cada variável
    imagens_lado_a_lado = cv2.hconcat([img_bgr, img_equalizada_bgr])

    # Exibir o resultado
    cv2.imshow('Antes (Esquerda) e Depois (Direita)', imagens_lado_a_lado)

    # Manter a janela aberta até que qualquer tecla seja pressionada
    cv2.waitKey(0)
    
    # Fechar as janelas do OpenCV após a tecla ser pressionada
    cv2.destroyAllWindows()

# Usando o caminho corrigido com o 'r' antes das aspas
equalizar_imagem (c:/Users/Toni/Desktop/Trabalho T3/Supreme_pizza.jpg)