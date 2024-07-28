from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI()

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

productos = []

@app.get('/')
def index():
    return {'mensaje':'Bienvenidos a la API de productos'}

@app.get('/producto')
def obtener_productos():
    return productos

#funcion para crear productos 
# post = create

@app.post('/producto')
def crear_producto(producto: Producto):
    producto.id = str(uuid()) #retorna el resultado de la funcion uuid como id
    productos.append(producto)
    return {'mensaje':'producto creado satisfactoriamente'}

#funcion para buscar un producto desde el id

@app.get('/producto/{producto_id}')
def obtener_producto_id(producto_id: str):
    #otra forma de efectuar una busqueda de una lista es por medio de
    # la funcion filter
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    if len(resultado):
        return resultado[0]

    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado')

#funcion que permite eliminar un registro atravez de su id

@app.delete('/producto/{producto_id}')
def eliminar_producto_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    if len(resultado):
        producto = resultado[0]
        productos.remove(producto)

        return {'mensaje': f'El producto con ID {producto_id} fue eliminado'}
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado')

@app.put('/produto/{producto_id}')
def actualizar_producto(producto_id:str, producto:Producto):
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    if len(resultado):
        producto_encontrado = resultado[0]
        producto_encontrado.nombre = producto.nombre #variable con datos nuevos
        producto_encontrado.precio_compra = producto.precio_compra
        producto_encontrado.precio_venta = producto.precio_venta
        producto_encontrado.proveedor = producto.proveedor
        return producto_encontrado
    
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado')