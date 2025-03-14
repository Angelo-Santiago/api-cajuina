# pedidos/impressao.py

from escpos.printer import Usb
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Função para imprimir o ticket na impressora térmica
def imprimir_ticket(pedido):
    try:
        printer = Usb(0x04b8, 0x0202, 0)  # Substitua pelos IDs da sua impressora
        printer.set(align='center', font='b', height=2, width=2)
        printer.text(f"Pedido #{pedido['id']}\n")
        printer.text(f"Produto: {pedido['produto']}\n")
        printer.text(f"Quantidade: {pedido['quantidade']}\n")
        printer.text(f"Preço: R$ {pedido['preco']:.2f}\n")
        printer.text(f"Observações: {pedido['observacoes']}\n")
        printer.cut()
        print("Ticket impresso com sucesso!")
    except Exception as e:
        print(f"Erro ao imprimir o ticket: {e}")


# Função para gerar e salvar um PDF do pedido
def gerar_pdf(pedido, nome_arquivo='ticket_pedido.pdf'):
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, altura - 100, f"Pedido #{pedido['id']}")
    c.setFont("Helvetica", 12)
    c.drawString(100, altura - 120, f"Produto: {pedido['produto']}")
    c.drawString(100, altura - 140, f"Quantidade: {pedido['quantidade']}")
    c.drawString(100, altura - 160, f"Preço: R$ {pedido['preco']:.2f}")
    c.drawString(100, altura - 180, f"Observações: {pedido['observacoes']}")

    c.save()
    print(f"PDF gerado: {nome_arquivo}")
